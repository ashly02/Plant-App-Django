from django.db import models

# Create your models here.
class Registerdb(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=10)

class Bookingdb(models.Model):
    name=models.CharField(max_length=20)
    address=models.TextField()
    phone=models.IntegerField()
    plant=models.CharField(max_length=30)