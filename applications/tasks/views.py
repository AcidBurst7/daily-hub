from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board, Column
from .forms import BoardEditForm, ColumnEditForm

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
    if request.method == 'POST':
        create_board_form = BoardEditForm(request.POST)
        if create_board_form.is_valid():
            cleaned_data = create_board_form.cleaned_data
            board = Board.objects.filter(id=board_id).first()
            board.name = cleaned_data["name"]
            board.save()
            return redirect("tasks:index")

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
    # return render(request, 'tasks/index.html', {
    #         'create_column_form': ColumnEditForm(),
    #         'data': get_user_boards(request.user),
    #     }
    # )

@login_required
def edit_column(request, column_id: int):
    if request.method == 'POST':
        create_column_form = ColumnEditForm(request.POST)
        if create_column_form.is_valid():
            cleaned_data = create_column_form.cleaned_data
            column = Column.objects.filter(id=column_id).first()
            column.name = cleaned_data["name"]
            column.save()
            return redirect("tasks:index")
        
@login_required
def delete_column(request, column_id: int):
    if request.method == 'POST':
        Column.objects.filter(id=column_id).delete()
        return redirect("tasks:index")