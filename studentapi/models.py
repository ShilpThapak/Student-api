from django.db import models

# Create your models here.
class Student(models.Model):
   roll = models.CharField(max_length=3)
   fullname = models.CharField(max_length=100)
