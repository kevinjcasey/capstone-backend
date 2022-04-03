from django.shortcuts import render
from rest_framework import generics
from .serializers import UsersSerializer
from .models import Users

from .serializers import TriviaSerializer
from .models import Trivia

class UsersList(generics.ListCreateAPIView):
  queryset = Users.objects.all().order_by('id')
  serializer_class = UsersSerializer

class UsersDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Users.objects.all().order_by('id')
  serializer_class = UsersSerializer

## Trivia 
class TriviaList(generics.ListCreateAPIView):
  queryset = Trivia.objects.all()order_by('id')
  serializer_class = TriviaSerializer

class TriviaList(generics.RetrieveUpdateDestroyAPIView):
  queryset = Trivia.objects.all()order_by('id')
  serializer_class = TriviaSerializer