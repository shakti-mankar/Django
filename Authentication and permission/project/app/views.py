
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication] ## objecte level authentication
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer