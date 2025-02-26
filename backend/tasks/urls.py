from django.urls import path
from .views import create_view, list_tasks

app_name = "tasks"

urlpatterns = [
    path('create-task/', create_view, name='create-task'),
    path('', list_tasks, name='list-tasks')
]