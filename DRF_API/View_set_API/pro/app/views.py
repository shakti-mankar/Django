from django.shortcuts import render
from .models import Student,officers

from django.shortcuts import get_object_or_404
from .serializers import StudentSerializer , OfficersSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
   
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class OfficersViewset(viewsets.ModelViewSet):

#     queryset = officers.objects.all()
#     serializer_class = OfficersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class OfficersViewset(viewsets.ModelViewSet):
    queryset = officers.objects.all()
    serializer_class = OfficersSerializer
