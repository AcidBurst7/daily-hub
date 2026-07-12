from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("create_board/", views.create_board, name="create_board"),
    path("create_column/<int:board_id>/", views.create_column, name="create_column"),
    path("columns/<int:board_id>/", views.create_board, name="get_columns"),
    # path("/{id}", views.task, name="task")
]
