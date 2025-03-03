from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('new/', views.create_task, name='create-task'),
    path('', views.list_tasks, name='list-tasks'),
    path('<int:pk>/detail/', views.task_detail, name="task-detail"),
    path('<int:pk>/delete/', views.delete_task, name="delete-task"),
    path('<int:pk>/update/', views.update_task, name='update-task'),
]
