from django.db import models

# Create your models here.
class ccontactme(models.Model):
    name=models.CharField(default=" ",max_length=50)
    email=models.EmailField()
    message=models.CharField(max_length=7000)

class addprojects(models.Model):
    techdata=models.CharField(default=" ",max_length=10000)
    head=models.CharField(default=" ",max_length=10000)
    link=models.CharField(default=" ",max_length=10000)

class mydata(models.Model):
    name=models.CharField(default=" ",max_length=10000)
    image=models.ImageField(upload_to='myianges',default=" ")
    Address=models.CharField(max_length=100000,default=" ")
    age=models.IntegerField(default=0)
    email=models.EmailField()
    Phonenumber=models.IntegerField(default=0)
    Skills=models.CharField(default=" ",max_length=100000)
    Collegename=models.CharField(default=" ",max_length=10000)
    media = models.FileField(null=True, blank=True,upload_to ='uploads/')
    
class resgister(models.Model):
      name=models.CharField(default=" ",max_length=100000)
      email=models.EmailField()
      passwords=models.CharField(default=" ",max_length=100000)
    
