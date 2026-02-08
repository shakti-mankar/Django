"""
URL configuration for myproject project.

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
from myapp import views
urlpatterns = [

    # admin
    path('admin/', admin.site.urls),
    path('', views.landing,name='landing'),
    path('login', views.login,name='login'),
    path('admindpanel',views.admindpanel,name='admindpanel'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('sin',views.sin,name='sin'),
    path('free',views.free,name='free'),
    path('xbox',views.xbox,name='xbox'),
    path('save_department',views.save_department,name='save_department'),
    path('addemp',views.addemp,name='addemp'),
    path('add_anlytics',views.add_anlytics,name='add_anlytics'),
    path('add_setting',views.add_setting,name='add_setting'),


    path('add_employees',views.add_employees,name='add_employees'),
    path('all_employees',views.all_employees,name='all_employees'),
    path('remove_employees',views.remove_employees,name='remove_employees'),
    path('remove_department',views.remove_department,name='remove_department'),
    
    path('add_department',views.add_department,name='add_department'),
    path('all_department',views.all_department,name='all_department'),
    path('all_quries',views.all_quries,name='all_quries'),
    path('payroll',views.payroll,name='payroll'),



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
    path("profile",views.profile,name="profile")

















    













]
