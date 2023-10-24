from django.db import models
from user.models import User
class event_R (models.Model):
    
    STATUS_EVENT = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('WAITING_FOR_RESPONSE', 'Waiting for Response'),
        ('WAITING_FOR_HANDLING', 'Waiting for Handling'),
    )

    start_date = models.DateTimeField(auto_now_add=True)  
    end_date = models.DateTimeField()  
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    status = models.CharField( max_length= 50,choices=STATUS_EVENT ,default='Open')  

    is_draft = models.CharField()  
    archived = models.BooleanField(default=False)  

    shared_users = models.ManyToManyField(User, related_name='shared_events')  

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')

class event_chat(event_R):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

class event_file(event_R):  
    upload_file_date = models.DateTimeField(auto_now_add=True)  
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)  
    file = models.FileField()
