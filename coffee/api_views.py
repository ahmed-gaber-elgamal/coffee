from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer
from .models import CoffeeMachine, CoffeePod
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.exceptions import ValidationError

# class ProductsPagination(LimitOffsetPagination):
#     default_limit = 10
#     max_limit = 100


class CoffeeMachineList(ListAPIView):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends =(DjangoFilterBackend,)
    filter_fields = ('id','product_type', 'water_line_compatible')


class CoffeePodList(ListAPIView):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends =(DjangoFilterBackend,)
    filter_fields = ('id', 'product_type', 'coffee_flavor','pack_size')