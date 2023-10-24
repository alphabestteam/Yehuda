from rest_framework import serializers
from user.models import User

class userSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)  
    id_number = serializers.CharField(max_length=9)  
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields  =  '__all__'