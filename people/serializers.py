from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields ='__all__'
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.id = validated_data.get('id', instance.id)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.hometown = validated_data.get('hometown', instance.hometown)
        instance.save()
        return instance