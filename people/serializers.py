from rest_framework import serializers
from .models import Person, Parent

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields ='__all__'
        
class parentSerializer(PeopleSerializer):
    class Meta:
        model = Parent
        fields ='__all__'
    