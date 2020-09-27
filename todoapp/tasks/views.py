from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoItem
from .forms import AddTaskForm, ToDoItemFormModel


def index(requests):
    return HttpResponse("Hello guest")


def tasks_list(requests):
    f = AddTaskForm()
    all_tasks = ToDoItem.objects.all()
    return render(requests, 'tasks/lists.html', {'tasks': all_tasks, 'form': f})


def complete_task(requests, uid):
    t = ToDoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse('Ok')


def delete_task(requests, uid):
    t = ToDoItem.objects.get(id=uid)
    t.delete()
    return redirect('/tasks/lists')


def add_tasks(requests):
    if requests.method == "POST":
        form = ToDoItemFormModel(requests.POST)
        if form.is_valid():
            form.save()
    else:
        form = ToDoItemFormModel
    return redirect('/tasks/lists')

