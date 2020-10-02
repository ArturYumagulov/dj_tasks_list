from django.urls import path

from .views import index, TaskListView, complete_task, delete_task, TaskCreateView, TaskDetailView, TaskEditView

app_name = "tasks"

urlpatterns = [
    path('', index, name='index'),
    path('lists/', TaskListView.as_view(), name='list'),
    path('complete/<int:uid>', complete_task, name='complete'),
    path('edit/<int:pk>', TaskEditView.as_view(), name='edit'),
    path('delete/<int:uid>', delete_task, name='delete'),
    path('create/', TaskCreateView.as_view(), name='add_task'),
    path('details/<int:pk>', TaskDetailView.as_view(), name="details"),
]
