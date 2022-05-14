from unicodedata import name
from django.db import models
class contact_us(models.Model):
    yourname=models.CharField(max_length=200)
    youremail=models.CharField(max_length=200)
    yourphone=models.CharField(max_length=200)
    yourproblem=models.CharField(max_length=200)
class bookin(models.Model):
    Name=models.CharField(max_length=200)
    Phone=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Today=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    Places=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    Enddate=    models.CharField(max_length=200,null=True)
class booket(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Phone=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=200,null=True)
    Today=models.CharField(max_length=200,null=True)
    State=models.CharField(max_length=200,null=True)
    Places=models.CharField(max_length=200,null=True)
    Date=models.CharField(max_length=200,null=True)
    Enddate=models.CharField(max_length=200,null=True)