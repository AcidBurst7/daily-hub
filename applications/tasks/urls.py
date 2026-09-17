from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),

    # Доски
    path("create_board/", views.create_board, name="create_board"),
    path("edit_board/<int:board_id>", views.edit_board, name="edit_board"),
    path("delete_board/<int:board_id>", views.delete_board, name="delete_board"),

    # Колонки
    path("create_column/<int:board_id>/", views.create_column, name="create_column"),
    path("edit_column/<int:column_id>/", views.edit_column, name="edit_column"),
    path("delete_column/<int:column_id>/", views.delete_column, name="delete_column"),

    # Задачи
    path("create_task/<int:column_id>/", views.create_task, name="create_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("move_task/", views.move_task, name="move_task"),
    path("task/<int:task_id>/complete/", views.complete_task, name="complete_task"),

    path("clear_modal/", views.clear_modal, name="clear_modal"),

    # Чеклисты
    path("create_checklist/<int:task_id>/", views.create_checklist, name="create_checklist"),
    path("edit_checklist/<int:checklist_id>/", views.edit_checklist, name="edit_checklist"),
    path("checklist/<int:checklist_id>/title/", views.get_checklist_title, name="get_checklist_title"),
    path("delete_checklist/<int:checklist_id>/", views.delete_checklist, name="delete_checklist"),

    # Пункты чеклиста
    path("checklist/<int:checklist_id>/item/form/", views.create_checklist_item_form, name="create_checklist_item_form"),
    path("checklist/item/form/clear/", views.clear_checklist_item_form, name="clear_checklist_item_form"),
    path("checklist/<int:checklist_id>/item/create/", views.create_checklist_item, name="create_checklist_item"),
    path("checklist/item/<int:item_id>/toggle/", views.toggle_checklist_item, name="toggle_checklist_item"),
    path("checklist/item/<int:item_id>/delete/", views.delete_checklist_item, name="delete_checklist_item"),
]
