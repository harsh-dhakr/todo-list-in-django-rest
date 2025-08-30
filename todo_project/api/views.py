
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]   # dev: open API



def home(request):
    return render(request, "index.html")
