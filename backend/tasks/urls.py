from django.urls import path
from . import views
from rest_framework import routers
from tasks.viewsets import TaskViewSet

app_name = "tasks"

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path("", views.index, name="index"),
    path('new/task/', views.create_task, name='create-task'),
    path('tasks/', views.list_tasks, name='list-tasks'),
    path('<int:pk>/detail/task/', views.task_detail, name="task-detail"),
    path('<int:pk>/delete/task/', views.delete_task, name="delete-task"),
    path('<int:pk>/update/task/', views.update_task, name='update-task'),
] + router.urls
