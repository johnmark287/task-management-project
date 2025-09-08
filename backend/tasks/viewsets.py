from rest_framework import viewsets
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
   serializer_class = TaskSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
       return Task.objects.filter(user=self.request.user)

   def perform_create(self, serializer):
       serializer.save(user=self.request.user)