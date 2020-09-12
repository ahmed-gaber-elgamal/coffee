from django.shortcuts import render

# from .models import CoffeeMachine, CoffeePod

def index(request):
    # context = {
    #     'products': Product.objects.all(),
    # }
    return render(request, 'coffee/index.html')