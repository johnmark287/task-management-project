from rest_framework import serializers
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["first_name", "last_name", "username", "email", "password", "bio"]

class TaskSerializer(serializers.ModelSerializer):
# user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
  class Meta:
    model = Task
    fields = ["id", "user", "title", "description", "priority", "due_date", "status"]
    read_only_fields = ["id", "created_at"]
