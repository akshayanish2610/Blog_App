from django.db import models

# Create your models here.
class BlogModel(models.Model):
    user_id=models.CharField(default="",max_length=100)
    title=models.CharField(default="",max_length=100)
    msg=models.CharField(default="",max_length=200)
