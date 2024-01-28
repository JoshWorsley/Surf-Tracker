from rest_framework import serializers

from .models import Session, Surfer

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields ="__all__"

class SurferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surfer
        fields ="__all__"

class CreateSurferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surfer
        fields ="__all__"

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields =("Spot","Wind","rating","Tide")