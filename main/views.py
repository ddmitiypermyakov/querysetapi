from django.shortcuts import render
from .models import Auto, Brand, Detail


# Create your views here.

def home_page(request):
    auto = Auto.objects.filter(pk=2)
    print(auto.query)
    print(auto[0].brand)
    # print(dir(Auto.objects))


    context = {}
    return render(request, 'main/index.html', context)
