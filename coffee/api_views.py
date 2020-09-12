from rest_framework.generics import ListAPIView
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer
from .models import CoffeeMachine, CoffeePod
from django_filters.rest_framework import DjangoFilterBackend


class CoffeeMachineList(ListAPIView):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product_type', 'water_line_compatible', 'model_type')


class CoffeePodList(ListAPIView):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product_type', 'coffee_flavor', 'pack_size')
