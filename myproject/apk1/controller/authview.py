
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from apk1.forms import UserRegisterForm
from apk1.models import *
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully!')
            #image= form.cleaned_data.get('img')
            #messages.success(request, f'{image}')
            return redirect('/main.html')
    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})

def loginpage(request):
     if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/main.html')
     else:
         if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            user = authenticate(request, username=name, password=passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("main.html")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
            

         return render(request, "auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out")
    return redirect("main.html")

