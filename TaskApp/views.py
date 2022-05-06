from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .Serializers import TasSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TasSerializer
