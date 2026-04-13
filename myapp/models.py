from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class authority(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    
class user_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE) 
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    image=models.FileField()
    ward=models.IntegerField()
    place=models.CharField(max_length=100)
    pin=models.IntegerField()
    post=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
   
    
class request_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    image=models.FileField()
    descreption=models.CharField(max_length=50)
    date=models.DateField()
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
class assign_authority(models.Model):
    REQUEST=models.ForeignKey(request_table,on_delete=models.CASCADE)
    AUTHORITY=models.ForeignKey(authority,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=50)
class feedback(models.Model):
    ASSIGN=models.ForeignKey(assign_authority,on_delete=models.CASCADE)
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=50)
    ratings=models.FloatField()
    date=models.DateField()
    


    
    
        