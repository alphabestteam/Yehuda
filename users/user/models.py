from django.db import models
from django.core.exceptions import ValidationError

class UserWife(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User (models.Model):

    def clean(self):
        if "example.com" in self.email:
            raise ValidationError("Emails from example.com are not allowed.")
        
    username = models.CharField(max_length=100, blank=True, default='')  
    email = models.EmailField(validators=[clean])
    password = models.CharField(max_length=100, blank=True, default='')
    wife = models.ForeignKey(UserWife, on_delete=models.CASCADE)
    