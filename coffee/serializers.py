from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = ('sku_number', 'product_type', 'water_line_compatible', 'model_type')


class CoffeePodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePod
        fields = ('sku_number', 'product_type', 'coffee_flavor', 'pack_size')
