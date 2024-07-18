from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "created_at", "updated_at"]




class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "title", "description"]
