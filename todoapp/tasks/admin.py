from django.contrib import admin

from .models import ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created')
