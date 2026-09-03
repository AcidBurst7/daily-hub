from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("create_board/", views.create_board, name="create_board"),
    path("edit_board/<int:board_id>", views.edit_board, name="edit_board"),
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

    path("create_checklist/<int:task_id>/", views.create_checklist, name="create_checklist"),

    path("edit_checklist_name/<int:checklist_id>/", views.edit_checklist_name, name="edit_checklist_name"),
    path("delete_checklist/<int:checklist_id>/", views.delete_checklist, name="delete_checklist"),
    path("create_checklist_item_form/<int:checklist_id>/", views.create_checklist_item_form, name="create_checklist_item_form"),
    path("create_checklist_item/<int:checklist_id>/", views.create_checklist_item, name="create_checklist_item"),
    path("clear_checklist_item_form/", views.clear_checklist_item_form, name="clear_checklist_item_form"),
    
    path("toggle_checklist_item/<int:item_id>/",
        views.toggle_checklist_item,
        name="toggle_checklist_item"),

    path("delete_checklist_item/<int:item_id>/",
        views.delete_checklist_item,
        name="delete_checklist_item"),

    path(
        "checklist_create_form/<int:task_id>/",
        views.checklist_create_form,
        name="checklist_create_form",
    ),
    path("clear_checklist_form/", views.clear_checklist_form, name="clear_checklist_form"),

]
