from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# 🔹 Register
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            role=data['role']
        )
        return Response({"msg": "User Created"})

# 🔹 Login
class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "role": user.role
            })
        return Response({"error": "Invalid credentials"})

# 🔹 Jobs CRUD
class JobView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        return Response(JobSerializer(jobs, many=True).data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class JobDetail(APIView):
    def put(self, request, id):
        job = Job.objects.get(id=id)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        Job.objects.get(id=id).delete()
        return Response({"msg": "Deleted"})

# 🔹 Apply Job
class ApplyJob(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)