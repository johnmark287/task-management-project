from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from api import serializers
from tasks.models import Task
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

# Create your views here.
def index(request):
  return render(request, "api/index.html", {})
  
class UserViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = User.objects.all()
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['username', 'email']
  ordering_fields = ['username', 'date_joined']
  ordering = ['username']
  pagination_class = PageNumberPagination

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = serializers.TaskSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['due_date', 'status', 'priority']
  search_fields = ['title', 'description']
  ordering_fields = ['due_date', 'priority', 'created_at']
  ordering = ['due_date']
  pagination_class = PageNumberPagination
  
  def get_queryset(self):
    """Returns queryset of tasks created by the currently logged in user."""
    return Task.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    """Assigns task to the logged-in user automatically"""
    serializer.save(user=self.request.user)

  # @action(detail=False, methods=['get'])
  # def bulk_delete(self, request):
  #   """Deletes multiple tasks based on a list of IDs provided in the query parameters."""
  #   ids = request.query_params.get('ids', '')
  #   id_list = [i for i in ids.split(',') if i.isdigit()]
  #   if not id_list:
  #       return Response({'deleted': 0, 'error': 'No valid IDs provided.'}, status=status.HTTP_400_BAD_REQUEST)
  #   tasks_to_delete = self.get_queryset().filter(id__in=id_list)
  #   deleted_count = tasks_to_delete.count()
  #   tasks_to_delete.delete()
  #   return Response({'deleted': deleted_count}, status=status.HTTP_200_OK)
  