from django.shortcuts import render
from .models import Auto, Brand, Detail
from django.db.models import F,Count,Sum,Avg


# Create your views here.

def home_page(request):








    context = {}
    return render(request, 'main/index1.html', context)
