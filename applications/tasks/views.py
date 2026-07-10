from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Board, Task, Column
from .forms import BoardEditForm


def get_user_boards(user):
    return (
        Board.objects
        .filter(user=user)
        .prefetch_related("columns__tasks")
    )


@login_required
def index(request):
    tasks = get_user_boards(request.user)
    return render(
        request,
        'tasks/index.html',
        {'section': 'tasks', 'data': tasks}
    )


@login_required
def create_board(request):
    if request.method == 'POST':
        form = BoardEditForm(request.POST)
        if form.is_valid():
            form.save()
            tasks = get_user_boards(request.user)
            return render(
                request,
                'tasks/index.html',
                {'section': 'tasks', 'data': tasks}
            )
    form = BoardEditForm()
    return render(
        request,
        'tasks/create_board.html',
        {'form': form}
    )