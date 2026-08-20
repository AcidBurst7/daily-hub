import json
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from .models import Board, Column, Task, CheckList, CheckListItem
from .forms import (
    BoardEditForm, 
    ColumnEditForm, 
    TaskEditForm,
    ChecklistEditForm,
    ChecklistItemEditForm,
)

def get_user_boards(user):
    return (
        Board.objects
        .filter(user=user)
        .prefetch_related("columns__tasks")
    )


@login_required
def index(request):
    boards = Board.objects.filter(user=request.user)
    columns = get_user_boards(request.user)
    active_board = request.GET.get("board")
    return render(
        request,
        'tasks/index.html',
        {
            'section': 'tasks', 
            'boards': boards,
            'columns': columns,
            'active_board': int(active_board) if active_board else None,
            'data': get_user_boards(request.user),
            'create_board_form': BoardEditForm(),
            'create_column_form': ColumnEditForm(),
        }
    )

@login_required
def columns(request, board_id: int):
    columns = Column.objects.filter(board=board_id)
    return render(
        request,
        'tasks/index.html',
        {
            'section': 'tasks', 
            'columns': columns,
            'data': get_user_boards(request.user),
            'create_board_form': BoardEditForm()
        }
    )

@login_required
def create_board(request):
    board = None
    if request.method == 'POST':
        form = BoardEditForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            board=Board(
                name=cleaned_data["name"], 
                user=request.user
            )
            board.save()

            response = HttpResponse()
            response["HX-Redirect"] = f"{reverse("tasks:index")}?board={board.id}"
            return response
    return render(request, 'tasks/index.html', {
            'create_board_form': BoardEditForm(),
            'data': get_user_boards(request.user),
            'is_new': True,
            'board': board,
            "board_id": board.id if board else 0,
        }
    )

@login_required
def edit_board(request, board_id=0):
    board = None

    if board_id:
        board = get_object_or_404(
            Board,
            id=board_id,
            user=request.user
        )

    if request.method == "POST":
        form = BoardEditForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]

            if board:
                # Редактирование
                board.name = name
                board.save(update_fields=["name"])
            else:
                # Создание
                board = Board.objects.create(
                    name=name,
                    user=request.user
                )

            response = HttpResponse()
            response["HX-Redirect"] = (
                f"{reverse('tasks:index')}?board={board.id}"
            )
            return response

    else:
        form = BoardEditForm(
            initial={"name": board.name if board else ""}
        )

    return render(
        request,
        "tasks/partials/forms/edit_board.html",
        {
            "edit_board_form": form,
            "is_new": board is None,
            "board": board,
            "board_id": board.id if board else 0,
        }
    )

@login_required
def clear_modal(request):
    return HttpResponse("")

@login_required
def delete_board(request, board_id: int):
    if request.method == 'POST':
        Board.objects.filter(id=board_id).delete()
    return redirect("tasks:index")

@login_required
def create_column(request, board_id: int):
    if request.method == 'POST':
        create_column_form = ColumnEditForm(request.POST)
        if create_column_form.is_valid():
            cleaned_data = create_column_form.cleaned_data
            current_board = Board.objects.filter(id=board_id).first()
            new_colum = Column(
                name=cleaned_data["name"], 
                board=current_board
            )
            new_colum.save()
            return redirect(f"{reverse("tasks:index")}?board={new_colum.board.id}")

@login_required
def edit_column(request, column_id: int):
    column = get_object_or_404(
        Column,
        id=column_id,
        board__user=request.user
    )
    
    if request.method == 'POST':
        form = ColumnEditForm(request.POST)
        if form.is_valid():
            column.name = form.cleaned_data["name"]
            column.save(update_fields=["name"])

            response = HttpResponse()
            response["HX-Redirect"] = f"{reverse("tasks:index")}?board={column.board.id}"
            return response
    else:
        form = ColumnEditForm(
            initial={"name": column.name}
        )
        
    return render(
        request, 
        'tasks/partials/forms/edit_column.html', 
        {
            'edit_column_form': form,
            'column': column,
        }
    )
        
@login_required
def delete_column(request, column_id: int):
    if request.method == 'POST':
        column = Column.objects.get(id=column_id)
        column.delete()
        return redirect(f"{reverse("tasks:index")}?board={column.board.id}")

@login_required
def create_task(request, column_id: int):
    column = get_object_or_404(
        Column, 
        id=column_id,
        board__user=request.user
    )
    
    if request.method == "POST":
        form = TaskEditForm(request.POST, board=column.board)
        form_checklist = ChecklistEditForm(request.POST)
        form_checklistitem = ChecklistItemEditForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.column = column
            task.order = column.tasks.count()  # добавляем в конец списка
            task.save()
            
            response = HttpResponse()
            response["HX-Redirect"] = f"{reverse("tasks:index")}?board={task.column.board.id}"
            return response
    
    form = TaskEditForm(board=column.board)
    form_checklist = ChecklistEditForm()
    form_checklistitem = ChecklistItemEditForm()
    return render(request, 'tasks/partials/forms/edit_task.html', {
            'form': form,
            'board_id': column.board.id,
            'form_checklist': form_checklist,
            'form_checklistitem': form_checklistitem,
            'column': column,
            'is_new': True,
        }
    )

@login_required
def edit_task(request, task_id: int):
    task = get_object_or_404(
        Task, 
        id=task_id
    )

    if request.method == "POST":
        form = TaskEditForm(
            request.POST, 
            instance=task, 
            board=task.column.board
        )
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response["HX-Redirect"] = f"{reverse("tasks:index")}?board={task.column.board.id}"
            return response
    else:
        form = TaskEditForm(
            instance=task, 
            board=task.column.board
        )

    return render(
        request,
        "tasks/partials/forms/edit_task.html",
        {
            "form": form,
            "board_id": task.column.board.id,
            "task": task,
            'is_new': False,
        },
    )

@login_required
@require_POST
def move_task(request):
    data = json.loads(request.body)

    task = get_object_or_404(
        Task, 
        id=data["task_id"], 
        column__board__user=request.user
    )

    column = get_object_or_404(
        Column,
        id=data["column_id"],
        board__user=request.user
    )

    task.column = column
    task.save()

    return JsonResponse({"status": True})

@login_required
def complete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(
            Task, id=task_id,
            column__board__user=request.user
        )

        if task.completed_at:
            task.completed_at = None
            completed = False
        else:
            task.completed_at = timezone.now()
            completed = True

        task.save(update_fields=["completed_at"])

        return JsonResponse({
            "completed": completed
        })

    return JsonResponse(
        {"error": "Invalid request"},
        status=400
    )

@login_required
def create_checklist(request, task_id: int):
    task = get_object_or_404(
        Task, 
        id=task_id,
        column__board__user=request.user
    )
    
    if request.method == "POST":
        checklist = CheckList()

        task.save(update_fields=["completed_at"])

        return JsonResponse({
            "completed": ...
        })

    return JsonResponse(
        {"error": "Invalid request"},
        status=400
    )

@login_required
def delete_task(request, task_id):
    task = Task.objects.filter(id=task_id).first()
    if request.method == "POST" and task:
        task.delete()
    return redirect(f"{reverse("tasks:index")}?board={task.column.board.id}")
