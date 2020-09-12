from django.contrib import admin
from .models import CoffeeMachine, CoffeePod


class CoffeeMachineAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'water_line_compatible')
    list_filter = ['product_type']
    search_fields = ['product_type']


class CoffeePodAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'coffee_flavor', 'pack_size')
    list_filter = ['product_type']
    search_fields = ['product_type']


admin.site.register(CoffeeMachine, CoffeeMachineAdmin)
admin.site.register(CoffeePod, CoffeePodAdmin)
