
from rest_framework import serializers
from .models import TextData

class TextDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextData
        # fields = ('text')
        fields="__all__"