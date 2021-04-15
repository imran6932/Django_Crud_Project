from django.db import models


# Create your models here.
class Student_user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    location = models.CharField(max_length=20)