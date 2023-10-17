from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key= True)
    date_of_birth =models.DateField()
    hometown = models.CharField(max_length=50)
# Create your models here.
