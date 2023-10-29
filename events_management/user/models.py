from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    id_number = models.CharField(max_length=15, primary_key= True)
    email = models.EmailField(unique=True)
    unread_messages = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

