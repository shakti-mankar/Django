from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('jobs/', JobView.as_view()),
    path('jobs/<int:id>/', JobDetail.as_view()),
    path('apply/', ApplyJob.as_view()),
]