from django.db import models

class User(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)  
    id_number = models.PositiveIntegerField(max_length=9, primary_key= True)  
    email = models.EmailField()
    un_read_messages = models.IntegerField()
