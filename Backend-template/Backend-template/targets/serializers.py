from rest_framework import serializers
from .models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'
        # define here your model and the fields to serialize

    def create(self, validated_data):
        return Target(**validated_data)
    
    def update(self, instance, validated_data):
        # Implement here an update function
        instance.name = validated_data.get('name',instance.name)
        instance.attack_priority = validated_data.get('attack_priority',instance.attack_priority)
        instance.longitude = validated_data.get('longitude',instance.longitude)
        instance.latitude = validated_data.get('latitude',instance.latitude)
        instance.enemy_organization = validated_data.get('enemy_organization',instance.enemy_organization)
        instance.target_goal = validated_data.get('target_goal',instance.target_goal)
        instance.target_id = validated_data.get('target_id',instance.target_id)
        instance.was_target_destroyed = validated_data.get('was_target_destroyed',instance.was_target_destroyed)
        instance.save()
        return instance
    