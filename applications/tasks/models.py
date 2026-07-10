from django.db import models
from django.conf import settings


class Board(models.Model):
    name = models.CharField(max_length=55)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="boards",
    )

    def __str__(self):
        return self.name


class Column(models.Model):
    board = models.ForeignKey(
        Board, 
        on_delete=models.CASCADE, 
        related_name="columns"
    )
    name = models.CharField(max_length=25)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["order"]


class Task(models.Model):
    column = models.ForeignKey(
        Column, 
        on_delete=models.CASCADE, 
        related_name="tasks"
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=7, default="#FFFFFF")
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["order"]
