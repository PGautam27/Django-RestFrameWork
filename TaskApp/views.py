from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset =