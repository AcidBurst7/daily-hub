from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("create_board/", views.create_board, name="create_board"),
    path("edit_board/<int:board_id>", views.edit_board, name="edit_board"),
    path("get_edit_board_form/<int:board_id>", views.get_edit_board_form, name="get_edit_board_form"),
    path("delete_board/<int:board_id>", views.delete_board, name="delete_board"),

    path("create_column/<int:board_id>/", views.create_column, name="create_column"),
    path("edit_column/<int:column_id>/", views.edit_column, name="edit_column"),
    path("delete_column/<int:column_id>/", views.delete_column, name="delete_column"),
    
    path("create_task/<int:column_id>/", views.create_task, name="create_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("move_task/", views.move_task, name="move_task"),
    path("task/<int:task_id>/complete/", views.complete_task, name="complete_task"),

    path("clear_modal/", views.clear_modal, name="clear_modal"),
]
