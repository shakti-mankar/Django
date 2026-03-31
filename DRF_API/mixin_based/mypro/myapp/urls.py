from django.urls import path
from myapp.views import Stu_List, Stu_Detail

urlpatterns = [
     
    # path('Stu_List/', Stu_List.as_view(), name='Stu_list'),
    # path('Stu_Detail/<int:pk>/', Stu_Detail.as_view(), name='Stu_Detail'),
    path('stu-list/', Stu_List.as_view(), name='stu-list'),
    path('stu-detail/<int:pk>/', Stu_Detail.as_view(), name='stu-detail'),
]