from django.urls import path
from .views import Stu_list, Stu_Detail

urlpatterns = [
    path('students/', Stu_list.as_view()),
    path('students/<int:pk>/', Stu_Detail.as_view()),
]