"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [


    # ADMIN 
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('admindash/', views.admindash, name='admindash'), 
    path('add_employee/',views.add_employee,name='add_employee'),
    path('logout/',views.logout,name='logout'),
    path('admin_dashcard/', views.admin_dashcard,name='admin_dashcard'),
    path('add_department/', views.add_department,name='add_department'),
    path('remove_employee/', views.remove_employee,name='remove_employee'),
    path('remove_department/', views.remove_department,name='remove_department'),
    path('all_employee/', views.all_employee,name='all_employee'),
    path('all_department/', views.all_department,name='all_department'),
    path('allquries/', views.all_quries,name='all_quries'),
    path('addemp/',views.addemp,name='addemp'),
    path('save_department/',views.save_department,name='save_department'),
    path("removeemp/<int:pk>/",views.removeemp,name="removeemp"),
    path("removedept/<int:pk>/",views.removedept,name="removedept"),
    



    # employees
    path('emppanel',views.emppanel,name='emppanel'),
    path('forget',views.forget,name='forget'),
    path("forgot_password",views.forgot_password,name='forgot_password'),
    path("newpassword",views.newpassword,name='newpassword'),
    path("otp",views.otp,name='otp'),
    path("newpass",views.newpass,name='newpass'),
    path("confirm",views.confirm,name='confirm'),
    path('resend_otp',views.resend_otp,name="resend_otp"),


    # qurey

    path("apply_query",views.apply_query,name='apply_query'),
    path("submit_query",views.submit_query,name="submit_query"),
    path("profile",views.profile,name="profile"),
    path("show_query",views.show_query,name="show_query"),
    path("a_reply/<int:pk>/",views.a_reply,name="a_reply"),
    path("reply_query/<int:pk>/",views.reply_query,name="reply_query"),
    path("pending_query",views.pending_query,name="pending_query"),
    path("done_query",views.done_query,name="done_query"),
    path("Edit/<int:pk>/",views.Edit,name="Edit"),
    path("Edit_query/<int:pk>/",views.Edit_query,name="Edit_query"),
    path("emppanel/Del/<int:pk>/",views.Del,name="Del"),
    path("removedept/<int:pk>/",views.removedept,name="removedept"),
    path("removeemp/<int:pk>/",views.removeemp,name="removeemp"),
    path("search/",views.search,name='search'),
    path("search1/",views.search1,name='search1'),





    
    
]

