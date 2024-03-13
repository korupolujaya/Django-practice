from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('__all__')


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        exclude=['nationality']
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieName
        fields = ['mname','director','actor']