from rest_framework import viewsets
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

#
class UserViewset(viewsets.ModelViewSet):
    serializer_class= UserSerializer
    queryset= User.objects.all()
#now we can use this userviewset inside our own urls.py
