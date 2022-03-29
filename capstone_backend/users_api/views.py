from django.shortcuts import render
from rest_framework import generics
from .serializers import UsersSerializer
from .models import Users

class UsersList(generics.ListCreateAPIView):
  queryset = Users.objects.all().order_by('id')
  serializer_class = UsersSerializer

class UsersDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Users.objects.all().order_by('id')
  serializer_class = UsersSerializer


