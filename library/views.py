from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F, Max,Count,Avg
from django.views.generic import View, CreateView
# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView
from .forms import CarForm, GetPost, MyFormNew, DimCarForm
from .models import *
# from .main.models import *
def home_page1(request):


    context = {

    }
    return render(request, 'index1.html',context)

class MyView(View):
    model = Book
    # template_name = 'index1.html'
    context_object_name = 'books'
    def put(self,request):
        return render(request,'index1.html')

class FormView(View):
    http_method_names = ['get', 'post', 'put']
    context_object_name = 'books'
    # template_name = 'index2.html'
    # def get(self,request):
        # if request.method  == 'get':
    def get(self,request):
        return render(request,'index2.html')

    def post(self,request):
        return print('Hello')

        # return render(request, 'index2.html')
    def put(self):
        print('Hello')
        return HttpResponse('Hello')

        # return HttpResponse('Hello')
    # def put(self,request):
    #
    #     return render(request,'index2.html')


class FormView1(CreateView):

    form_class=CarForm
    template_name='base.html'
    success_url = '/'

    # def clean_price(self):
    #
    #     price = int(self.cleaned_data['price'])*1.2
    #     self.cleaned_data['price']=price
    #     print(self.cleaned_data['price'])
    #     return self.cleaned_data['price']
    # def form_valid(self, form):
    #
    #     return super().form_valid()

def get_post_form(request):
    form = GetPost()
    if request.method  == 'POST':
        form = GetPost(request.POST)
        form.is_valid()
        print(form.errors())
        print(form.is_valid())


    context = {'form': form}
    return render(request,'getpost.html',context)

# class MyFormNew(CreateView):
#
#     form_class = MyForm
#     template_name = "new.html"


def my_form_new(request):
    form = MyFormNew()
    if request.method == 'POST':
        form = MyFormNew(request.POST)

        if form.is_valid():
            print(form)
            username = form.cleaned_data['username']
            print(username)
            return render(request, 'new.html', {'form': form})
        else:
            err = form.errors
            # print(err['email'])
            return render(request, 'new.html', {'form': form,'errors': err})

    else:
        form = MyFormNew()
        context = {'form' : form }
        return render(request,'new.html',context)

def dev_dims(requests,id):
    # form = DimCarForm(None or requests.POST)
    form = DimCarForm(initial={'brand': 'Brand', 'model' : 'coen', 'price' : '100'})
    if requests.method == 'POST':
        form = DimCarForm(requests.POST, instance=Car.objects.get(pk=id))
        # form.save()
        if form.is_valid():
            # print(form.cleaned_data())
            form.save()
    context={'form' : form}
    return render(requests,'newmodelform.html',context)