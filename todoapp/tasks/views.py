from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoItem
from .forms import ToDoItemFormModel
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse

def index(requests):
    return HttpResponse("Hello guest")


class TaskListView(ListView):
    queryset = ToDoItem.objects.all()
    context_object_name = "tasks"
    template_name = 'tasks/lists.html'


def complete_task(requests, uid):
    t = ToDoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse('Ok')


def delete_task(request, uid):
    t = ToDoItem.objects.get(id=uid)
    t.delete()
    return redirect('/tasks/lists')


class TaskCreateView(View):
    def post(self, request, *args, **kwargs):
        form = ToDoItemFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/lists/')
        return render(request, 'tasks/create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = ToDoItemFormModel()
        return render(request, 'tasks/create.html', {'form': form})


class TaskDetailView(DetailView):
    model = ToDoItem
    template_name = "tasks/details.html"


