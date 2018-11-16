from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
