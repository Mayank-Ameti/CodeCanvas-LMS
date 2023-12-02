

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from rest_framework import permissions
from.import models
from rest_framework.generics import RetrieveAPIView
from .models import Instructor
from .serializers import InstructorSerializer


class InstructorList(generics.ListCreateAPIView):
    queryset=models.Instructor.objects.all()
    serializer_class=InstructorSerializer
    permission_classes=[permissions.IsAuthenticated]


class InstructorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Instructor.objects.all()
    serializer_class=InstructorSerializer
    permission_classes=[permissions.IsAuthenticated]
