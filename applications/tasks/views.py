from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Board, Task, Column

@login_required
def index(request):
    tasks = (
            Board.objects
            .filter(user=request.user)
            .prefetch_related("columns__tasks")
        )
    return render(
        request,
        'tasks/index.html',
        {'section': 'tasks', 'data': tasks}
    )


@login_required
def create_board(request):
    if request.method == 'POST':
        ...
    return render(
        request,
        'tasks/create_board.html',
        {}
    )