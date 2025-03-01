from django.urls import path
from .views import create_task, list_tasks

app_name = "tasks"

urlpatterns = [
    path('new/', create_task, name='create-task'),
    path('', list_tasks, name='list-tasks')
]
