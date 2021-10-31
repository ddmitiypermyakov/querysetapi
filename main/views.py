from django.shortcuts import render
from .models import Auto, Brand, Detail


# Create your views here.

def home_page(request):
    auto = Auto.objects.filter()
    # print(auto.query)
    context = {}
    return render(request, 'main/index.html', context)
