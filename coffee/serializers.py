from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = ('product_type', 'water_line_compatible')


class CoffeePodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePod
        fields = ('product_type', 'coffee_flavor', 'pack_size')
