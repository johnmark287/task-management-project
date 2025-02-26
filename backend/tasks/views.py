# tasks/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm
from django.shortcuts import render, redirect

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def create_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task = Task.objects.create(title=title, description=description)
            task.save()
            return redirect("task-list")
        
        context = {
                "form": form,
        }
        return render(request, 'create_task.html', context)
    if request.method == "GET":
        form = TaskForm()
        context = {
            "form": form,
        }
    return render(request, 'task_list.html', context)

def list_tasks(request):
     tasks = Task.objects.all()
     print(tasks)
     return render(request, "list_tasks.html", { "tasks": tasks })
