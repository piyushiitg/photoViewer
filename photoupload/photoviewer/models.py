from django.db import models

# Create your models here.

class PhotoStorage(models.Model):
    photo_name = models.CharField(max_length=200)
    photo_path = models.CharField(max_length=200)
    storage_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class PhotoOwner(models.Model):
    photo_storage = models.ForeignKey(PhotoStorage)
    owner_name = models.CharField(max_length=200)
    owner_email = models.CharField(max_length=200)
    owner_account_user_name = models.CharField(max_length=200)
    owner_account_password = models.CharField(max_length=200)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')    
