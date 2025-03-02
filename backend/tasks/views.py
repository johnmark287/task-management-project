# tasks/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# class TaskViewSet(viewsets.ModelViewSet):
#    serializer_class = TaskSerializer
#    permission_classes = [IsAuthenticated]
#
#    def get_queryset(self):
#        return Task.objects.filter(user=self.request.user)
#
#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)

@login_required
def create_task(request):
    if request.method == "POST":
        print(f"††††††††††††††††")
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            print(f"†††††††† {task} ††††††††")
            return redirect(reverse("tasks:list-tasks"))
    if request.method == "GET":
        print(f"††††††††  ††††††††")
        form = TaskForm()
    return render(request, 'create_task.html', { "form": form })

@login_required
def list_tasks(request):
     tasks = Task.objects.all()
     return render(request, "list_tasks.html", { "tasks": tasks })
