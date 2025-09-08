from rest_framework import viewsets
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
   serializer_class = TaskSerializer
   permission_classes = [IsAuthenticated]
   filter_backends = [DjangoFilterBacked, filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['completed', 'due_date', 'status', 'priority']
   search_fields = ['title', 'description']
   ordering_fields = ['due_date', 'priority', 'created_at']
   ordering = ['due_date']
   
   def get_queryset(self):
       return Task.objects.filter(user=self.request.user)

   def perform_create(self, serializer):
       serializer.save(user=self.request.user)