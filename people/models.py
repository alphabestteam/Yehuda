from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key= True)
    date_of_birth =models.DateField()
    hometown = models.CharField(max_length=50)
# Create your models here.
class Parent(Person):
    work_space = models.CharField(max_length=50)
    salary = models.DecimalField(decimal_places=2,max_digits=15)
    child = models.ManyToManyField(Person, related_name= 'parents',default=[])
    
