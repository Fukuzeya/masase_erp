from django.db import models

# Create your models here.

sex = (
    ('Male','Male'),('Female','Female'),('Others','Others')
)

class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=12)
    gender = models.CharField(max_length=100,choices=sex)
    phone_number = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    