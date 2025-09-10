from rest_framework import viewsets, filters
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class TaskViewSet(viewsets.ModelViewSet):
   quesryset = Task.objects.all()   
   serializer_class = TaskSerializer
   permission_classes = [IsAuthenticated]
   filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['due_date', 'status', 'priority']
   search_fields = ['title', 'description']
   ordering_fields = ['due_date', 'priority', 'created_at']
   ordering = ['due_date']
   pagination_class = PageNumberPagination

   def get_queryset(self):
       return Task.objects.filter(user=self.request.user)

   def perform_create(self, serializer):
       serializer.save(user=self.request.user)