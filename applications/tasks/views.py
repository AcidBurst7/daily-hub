from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board, Column, Task
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
    return render(
        request,
        'tasks/index.html',
        {
            'section': 'tasks', 
            'boards': boards,
            'columns': columns,
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
    if request.method == 'POST':
        create_board_form = BoardEditForm(request.POST)
        if create_board_form.is_valid():
            cleaned_data = create_board_form.cleaned_data
            Board(
                name=cleaned_data["name"], 
                user=request.user
            ).save()
            return redirect("tasks:index")
    return render(request, 'tasks/index.html', {
            'create_board_form': BoardEditForm(),
            'data': get_user_boards(request.user),
        }
    )

@login_required
def edit_board(request, board_id: int):
    board = Board.objects.filter(id=board_id).first()
    edit_board_form = BoardEditForm(initial={"name": board.name})
    if request.method == 'POST':
        create_board_form = BoardEditForm(request.POST)
        if create_board_form.is_valid():
            cleaned_data = create_board_form.cleaned_data
            board = Board.objects.filter(id=board_id).first()
            board.name = cleaned_data["name"]
            board.save()
            return redirect("tasks:index")
    return render(request, 'tasks/forms/edit_board.html', {
            'edit_board_form': edit_board_form
        }
    )

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
            return redirect("tasks:index")

@login_required
def edit_column(request, column_id: int):
    column = Column.objects.filter(id=column_id).first()
    edit_column_form = ColumnEditForm(initial={"name": column.name})
    if request.method == 'POST':
        edit_column_form = ColumnEditForm(request.POST)
        if edit_column_form.is_valid():
            cleaned_data = edit_column_form.cleaned_data
            column = Column.objects.filter(id=column_id).first()
            column.name = cleaned_data["name"]
            column.save()
            return redirect("tasks:index")
    return render(request, 'tasks/forms/edit_column.html', {
            'edit_column_form': edit_column_form
        }
    )
        
@login_required
def delete_column(request, column_id: int):
    if request.method == 'POST':
        Column.objects.filter(id=column_id).delete()
    return redirect("tasks:index")

@login_required
def create_task(request, column_id: int):
    column = get_object_or_404(Column, id=column_id)
    
    if request.method == "POST":
        form = TaskEditForm(request.POST)
        form_checklist = ChecklistEditForm(request.POST)
        form_checklistitem = ChecklistItemEditForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.column = column
            task.order = column.tasks.count()  # добавляем в конец списка
            task.save()
            return redirect("tasks:index")
    
    form = TaskEditForm()
    form_checklist = ChecklistEditForm()
    form_checklistitem = ChecklistItemEditForm()
    return render(request, 'tasks/forms/edit_task.html', {
            'form': form,
            'form_checklist': form_checklist,
            'form_checklistitem': form_checklistitem
        }
    )

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:index")
    else:
        form = TaskEditForm(instance=task)

    return render(
        request,
        "tasks/forms/edit_task.html",
        {
            "form": form,
            "task": task,
            "is_edit": True,
        },
    )

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()

    return redirect("tasks:index")