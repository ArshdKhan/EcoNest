from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Neighbourhood_Info(models.Model):
    average_rent=models.IntegerField(default=0)
    neighbourhood= models.CharField(max_length=30,verbose_name="Neighbourhood")


    def __str__(self):
        return self.neighbourhood
