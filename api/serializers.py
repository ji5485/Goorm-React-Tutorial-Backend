from rest_framework import serializers
from .models import Phone, Counter

class PhoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Phone
    fields = '__all__'

class CounterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Counter
    fields = '__all__'