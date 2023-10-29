from rest_framework import serializers
from .models import message,Chat

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'