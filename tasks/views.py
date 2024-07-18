from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return TaskUpdateSerializer  # Replace CustomTaskSerializer with the name of your custom serializer
        else:
            return TaskSerializer