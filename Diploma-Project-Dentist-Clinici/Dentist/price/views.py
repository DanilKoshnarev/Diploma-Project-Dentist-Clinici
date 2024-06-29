from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def price_func(request):
    categories = Category.objects.all()   
    return render(request, 'price/price.html', context = {'categories': categories,'services': Service.objects.all()})