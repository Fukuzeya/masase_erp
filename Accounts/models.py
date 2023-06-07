from django.db import models

# Create your models here.



class Client(models.Model):
    ec_number = models.CharField(max_length=12,null=True, blank=True,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    #TODO: add other fields
    
