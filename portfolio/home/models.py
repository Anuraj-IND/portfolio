from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.CharField(max_length=12)
    message=models.TextField()
class user(models.Model): 
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)
class Admin_user(models.Model): 
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)       