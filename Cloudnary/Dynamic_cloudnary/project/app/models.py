from django.db import models

from cloudinary_storage.storage import MediaCloudinaryStorage,RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage

# Create your models here.

class Employee(models.Model):
	image = models.ImageField(upload_to='images/',storage=[MediaCloudinaryStorage])
	audio = models.FileField(upload_to='audio/',storage=[RawMediaCloudinaryStorage])
	video = models.FileField(upload_to='video/',storage=[VideoMediaCloudinaryStorage])
	
