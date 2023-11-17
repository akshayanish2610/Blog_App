from django.db import models

# Create your models here.
class BlogModel(models.Model):
    user_id=models.CharField(default="",max_length=100)
    title=models.CharField(default="",max_length=100)
    msg=models.CharField(default="",max_length=200)

class BlogRegistration(models.Model):
    name=models.CharField(default="",max_length=100)
    propic=models.CharField(default="",max_length=100)
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)
