from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.name
    
    

class Signup(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    phone=models.IntegerField(default='0')
    email=models.EmailField(default='')
    password=models.CharField(max_length=8)
    cpassword=models.CharField(max_length=8)
    def __str__(self):
        return self.fname
    
class Pro(models.Model):
    pname=models.CharField(max_length=10)
    des=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pro')
    review=models.TextField(max_length=50)
    

