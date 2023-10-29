from django.db import models
from user.models import User

class Chat(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    pass
    
class message(models.Model):
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
