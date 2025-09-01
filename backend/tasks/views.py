# tasks/views.py
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

@login_required(login_url="users/login/")
def index(request):
  user_id = request.user.id
  tasks = get_list_or_404(Task, user=request.user)
  return render(request, 'tasks/index.html', { "tasks": tasks, "user_id": user_id })

@login_required(login_url="/users/login/")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect(reverse("tasks:list-tasks"))
    if request.method == "GET":
        form = TaskForm()
    return render(request, 'tasks/create_task.html', { "form": form })

@login_required(login_url="/users/login/")
def list_tasks(request):
     tasks = get_list_or_404(Task, user=request.user)
     return render(request, "tasks/list_tasks.html", { "tasks": tasks })
@login_required(login_url="/users/login")
def task_detail(request, pk):
  task = Task.objects.get(pk=pk)
  return render(request, "tasks/task_detail.html", { "task": task })
  
@login_required(login_url="/users/login/")
def delete_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.delete()
  return render(request, "tasks/delete_task.html", { "task": task })

def update_task(request, pk):
  task = get_object_or_404(Task, pk=pk)

  if request.method == "POST":
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      messages.info(request, f"{ task } updated successfully.")
      return redirect(reverse('tasks:task-detail', args=[pk]))
  if request.method == "GET":
    form = TaskForm(instance=task)
  return render(request, "tasks/update_task.html", { "form": form, "task": task })
  