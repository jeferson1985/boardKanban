from django.shortcuts import render

from .models import Tasks

from rest_framework.viewsets import ModelViewSet

from .serializers import TasksSerializer


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer