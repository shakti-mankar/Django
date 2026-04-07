# from rest_framework import viewsets, permissions
# from .models import Job, Application
# from .serializers import JobSerializer, ApplicationSerializer


# # ================= JOB VIEWSET =================

# class JobViewSet(viewsets.ModelViewSet):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#     permission_classes = [permissions.AllowAny]  


# # ================= APPLICATION VIEWSET =================

# class ApplicationViewSet(viewsets.ModelViewSet):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer
#     permission_classes = [permissions.AllowAny]   





from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User , Job , Application
from django.shortcuts import get_object_or_404
from .serializers import JobSerializer ,ApplicationSerializer , UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

class JobViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Job.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication] objectt lvel 
    serializer_class = JobSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Application.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication] objectt lvel 
    serializer_class = ApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = User.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication] objectt lvel 
    serializer_class = UserSerializer
