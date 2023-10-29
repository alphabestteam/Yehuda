from rest_framework import serializers
from .models import Event , Event_file,Event_chat

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class EventFileSerializer(EventSerializer):
    class Meta:
        model = Event_file
        fields = '__all__'

class EventChatSerializer(EventSerializer):
    class Meta:
        model = Event_chat
        fields = '__all__'
        