from django.contrib import admin

from .models import Task, Column, Board


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'column', 'title',
        'description', 'order',
        'color', 'is_archived',
        'created_at', 'updated_at',
        'deadline', 'completed_at'
    ]
    list_filter = [
        'created_at', 'updated_at', 
        'deadline', 'completed_at'
    ]


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'board', 'order'
    ]


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
