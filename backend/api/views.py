from django.shortcuts import render
from rest_framework import viewsets, permissions
from api import serializers
from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def index(request):
  return render(request, "api/index.html", {})
  
class UserViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = User.objects.all()
  permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.TaskSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset(self):
    """Returns queryset of tasks created by the currently logged in user."""
#    return Task.objects.select_related("user")
    return Task.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    """Assigns task to the logged-in user automatically"""
    serializer.save(user=self.request.user)