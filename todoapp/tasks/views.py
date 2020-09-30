from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoItem
from .forms import ToDoItemFormModel
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(requests):
    return HttpResponse("Hello guest")


class TaskListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    # queryset = ToDoItem.objects.all()
    context_object_name = "tasks"
    template_name = 'tasks/lists.html'

    def get_queryset(self):
        u = self.request.user
        return u.tasks.all()


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
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('/tasks/lists/')

        return render(request, 'tasks/create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = ToDoItemFormModel()
        return render(request, 'tasks/create.html', {'form': form})


class TaskDetailView(DetailView):
    model = ToDoItem
    template_name = "tasks/details.html"


