from django.contrib.auth.models import User
from .serializers import StudentSerializers,UserSerializer
from .models import Student
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from django.shortcuts import render

class StudentView(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


