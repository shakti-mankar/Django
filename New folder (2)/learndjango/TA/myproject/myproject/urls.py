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



from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index,name='index'),
    path('data',views.data,name='data'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



# data.City 
# ''
# >>> data.delete()
# (1, {'app.Student': 1})
# >>> data=S.objects.get(id=6)
# >>> data.Name
# 'sanjay'
# >>> data.City
# 'indore'
# >>> data.Contact
# 798899780978
# >>> data.delete()
# (1, {'app.Student': 1})
# >>> data=S.objects.get(id=2)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\query.py", line 
# 639, in get
#     raise self.model.DoesNotExist(
#         "%s matching query does not exist." % self.model._meta.object_name
#     )
# app.models.Student.DoesNotExist: Student matching query does not exist.
# >>> data=S.objects.get(id=3) 
# >>> data.name
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'name'. Did you mean: 'Name'?
# >>> data.Name
# 'Neeraj'
# >>> data.email
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'email'. Did you mean: 'Email'?
# >>> data.Email
# ''
# >>> data.Contact
# 1234567898
# >>> data.Email="neerajsir@123.com"
# >>> data.Email   
# 'neerajsir@123.com'
# >>> data.save()
# >>> data.Eduction
# ''
# >>> data.Eduction="M.Teach"
# >>> data.Eduction
# 'M.Teach'
# >>> data.save()
# >>> data=S.objects.get(City='indore')
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\query.py", line 
# 642, in get
#     raise self.model.MultipleObjectsReturned(
#     ...<5 lines>...
#     )
# app.models.Student.MultipleObjectsReturned: get() returned more than one Student -- it returned 4!
# >>> data=S.objects.get(City='Bhopal') 
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\query.py", line 
# 639, in get
#     raise self.model.DoesNotExist(
#         "%s matching query does not exist." % self.model._meta.object_name
#     )
# app.models.Student.DoesNotExist: Student matching query does not exist.
# >>> data=S.objects.get(id=1)          
# >>> data 
# <Student: Student object (1)>
# >>> data.Name
# 'Sumit'
# >>> data.Name,data.Email,data.Contact
# ('Sumit', 'Sumitrajaksumitrajak793@gmail.com', 79987789)
# >>> data=S.objects.first()     
# >>> data
# <Student: Student object (1)>
# >>> S.objects.last()         
# <Student: Student object (5)>
# >>> S.objects.latest()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\query.py", line 
# 1133, in latest
#     return self.reverse()._earliest(*fields)
#            ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
#   File "C:\Users\DELL E5450\OneDrive\Desktop\Django\DTL_filter\env\Lib\site-packages\django\db\models\query.py", line 
# 1108, in _earliest
#     raise ValueError(
#     ...<2 lines>...
#     )
# ValueError: earliest() and latest() require either fields as positional arguments or 'get_latest_by' in the model's Meta.
# >>> S.objects.latest(Name)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'Name' is not defined
# >>> S.objects.latest('Name')
# <Student: Student object (4)>
# >>> S.objects.latest('Contact')
# <Student: Student object (5)>
# >>> S.objects.earliest('Contact')
# <Student: Student object (1)>
# >>> S.objects.earliest('Name')    
# <Student: Student object (3)>
# >>> S.objects.all()            
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>]>
# >>> S.objects.filter(City='indore')
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>]>
# >>> S.objects.filter(City='Bhopal') 
# <QuerySet []>
# >>> S.objects.order_by(City)          
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'City' is not defined
# >>> S.objects.order_by('City')
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>]>
# >>> S.objects.order_by('Name') 
# <QuerySet [<Student: Student object (3)>, <Student: Student object (5)>, <Student: Student object (1)>, <Student: Student object (4)>]>
# >>> S.objects.order_by(-'Name')
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: bad operand type for unary -: 'str'
# >>> S.objects.order_by('-Name') 
# <QuerySet [<Student: Student object (4)>, <Student: Student object (1)>, <Student: Student object (5)>, <Student: Student object (3)>]>
# >>> S.objects.exclude(Name='Neeraj')id==
# <QuerySet [<Student: Student object (1)>, <Student: Student object (4)>, <Student: Student object (5)>]>
# >>> S.objects.exclude(City='indore') 
# <QuerySet []>
# >>> S.objects.all()                  
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>]>
# >>> S.objects.all().values()
# <QuerySet [{'id': 1, 'Name': 'Sumit', 'Email': 'Sumitrajaksumitrajak793@gmail.com', 'Contact': 79987789, 'Eduction': '[]', 'City': 'indore', 'Gender': 'male', 'Image': 'done.png', 'Document': 'report.pdf', 'Audio': 'soccer-kick-6235.mp3', 'Video': 'website1.mp4'}, {'id': 3, 'Name': 'Neeraj', 'Email': 'neerajsir@123.com', 'Contact': 1234567898, 'Eduction': 'M.Teach', 'City': 'indore', 'Gender': '', 'Image': '', 'Document': '', 'Audio': '', 'Video': ''}, {'id': 4, 'Name': 'sumitrajak', 'Email': 'sumitrajaksumitrajak793@gmail.com', 'Contact': 234567898, 'Eduction': '[]', 'City': 'indore', 'Gender': 'male', 'Image': '', 'Document': '', 'Audio': '', 'Video': ''}, {'id': 5, 'Name': 'sid', 'Email': 'sumitrajaksumitrajak733@gmail.com', 'Contact': 8787998798, 'Eduction': '[]', 'City': 'indore', 'Gender': 'male', 'Image': 'profile_page_3.png', 'Document': 'report_sNWisYU.pdf', 'Audio': 'soccer-kick-6235_SQ8ENS0.mp3', 'Video': 'website1_fzTea5K.mp4'}]>
# >>> S.objects.all().valueslist()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'QuerySet' object has no attribute 'valueslist'. Did you mean: 'values_list'?
# >>> S.objects.all().values_list()
# <QuerySet [(1, 'Sumit', 'Sumitrajaksumitrajak793@gmail.com', 79987789, '[]', 'indore', 'male', 'done.png', 'report.pdf', 'soccer-kick-6235.mp3', 'website1.mp4'), (3, 'Neeraj', 'neerajsir@123.com', 1234567898, 'M.Teach', 'indore', '', '', '', '', ''), (4, 'sumitrajak', 'sumitrajaksumitrajak793@gmail.com', 234567898, '[]', 'indore', 'male', '', '', '', ''), (5, 'sid', 'sumitrajaksumitrajak733@gmail.com', 8787998798, '[]', 'indore', 'male', 'profile_page_3.png', 'report_sNWisYU.pdf', 'soccer-kick-6235_SQ8ENS0.mp3', 'website1_fzTea5K.mp4')]>
# >>>