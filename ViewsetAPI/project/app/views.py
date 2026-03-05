
# from django.shortcuts import render
from .models import Student
# from django.shortcuts import get_object_or_404
from .serializers import StudentSerializer
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.
# class StudentViewSet(viewsets.ViewSet):

#     def list(self, request):
#         snippets = Student.objects.all()
#         serializer = StudentSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk):
#         xyz = Student.objects.filter(id=pk)
#         if xyz:
#             snippet = Student.objects.get(id=pk)
#             serializer = StudentSerializer(snippet)
#             return Response(serializer.data)
#         else:
#             return Response({"error": "Student not found"},status=status.HTTP_404_NOT_FOUND)

#     def update(self, request, pk):
#         snippet = Student.objects.get(id=pk)
#         serializer = StudentSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk):
#         snippet = Student.objects.get(id=pk)
#         serializer = StudentSerializer(snippet, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk):
#         snippet = Student.objects.get(id=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   