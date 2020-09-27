from django.urls import path

from .views import index, tasks_list, complete_task, delete_task, add_tasks

urlpatterns = [
    path('', index, name='index'),
    path('lists/', tasks_list, name='lists'),
    path('complete/<int:uid>', complete_task, name='complete'),
    path('delete/<int:uid>', delete_task, name='delete'),
    path('add_task/', add_tasks, name='add_task')
]