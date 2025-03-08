from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path('new/task/', views.create_task, name='create-task'),
    path('tasks/', views.list_tasks, name='list-tasks'),
    path('<int:pk>/detail/task/', views.task_detail, name="task-detail"),
    path('<int:pk>/delete/task/', views.delete_task, name="delete-task"),
    path('<int:pk>/update/task/', views.update_task, name='update-task'),
]
