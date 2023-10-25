from django.contrib.auth.models import User
from .models import UserWife
from rest_framework import serializers
from datetime import datetime, timedelta


class MessageSerializer(serializers.ModelSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    
    wife = serializers.SlugRelatedField(slug_field='name', queryset=UserWife.objects.all())
        
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at']
    is_online = serializers.SerializerMethodField()
    is_new_user = serializers.SerializerMethodField()
    messages = MessageSerializer(many=True, read_only=True)


    def get_is_online(self, obj):
        return (datetime.now() - obj.last_login).total_seconds() <= 30
    
    def get_is_new_user(self, obj):
        seven_days_ago = datetime.now() - timedelta(days=7)
        return obj.created_at >= seven_days_ago

   
