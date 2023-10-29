from django.db import models
from user.models import User
from chat.models import Chat

EVENT_STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('waiting_response', 'Waiting for Response'),
    ('waiting_handling', 'Waiting for Handling'),
]

class Event(models.Model):
    opening_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    closing_date = models.DateTimeField(auto_now = True, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES , default="open")
    is_draft = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(User, related_name='shared_events',blank=True)

class Event_file(Event):
    opening_file_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/",blank=True,null=True ,default="")
    
class Event_chat(Event):
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)