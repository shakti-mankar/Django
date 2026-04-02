from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Job, JobApplication, User
from .serializers import JobSerializer, JobApplicationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

# JOB VIEWSET
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

    def get_queryset(self):
        if self.request.user.role == 'employer':
            return Job.objects.filter(employer=self.request.user)
        return Job.objects.all()


# APPLICATION VIEWSET
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)

    def get_queryset(self):
        if self.request.user.role == 'candidate':
            return JobApplication.objects.filter(candidate=self.request.user)
        return JobApplication.objects.all()


# USER REGISTER
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)