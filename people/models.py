from django.db import models
from datetime import datetime

class Person(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key= True)
    date_of_birth =models.DateField()
    hometown = models.CharField(max_length=50)
# Create your models here.
    def under_18(self):
        age_now = datetime.now().year - 18
        return self.date_of_birth.year <= age_now
            
class Parent(Person):
    work_space = models.CharField(max_length=50)
    salary = models.IntegerField()
    child = models.ManyToManyField(Person, related_name= 'parents',default=[])
    
