
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *


def say_hello(request):
    return render(request, 'main.html')

#def home(request):
    #return render(request, 'users/home.html')

def collections(request):
    category = Category.objects.all()
    #category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products =Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first
        context = {'products' : products, 'category_name':category_name}
        return render(request, "products/index.html", context)
    else:
        return redirect('collections.html')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products' : products,}
        else:
              messages.warning(request, "No such product was found.")    
              return redirect('collections.html')
    else:
        messages.warning(request, "No such category was found.")    
        return redirect('collections.html')
    return render(request, "products/view.html", context)
