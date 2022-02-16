from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . models import Product
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm

def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'pages/index.html', {'products':products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    productColors = product.productcolor_set.all()
   
    
    return render(request, 'pages/product-detail.html', {'productColors':productColors, 'product':product})


def sign_in(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
      
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            message = 'Такого пользователя не существует.'   
            return HttpResponse(message)
           
    else:
        return render(request, 'pages/sign_in.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            messages = ValidationError(list(form.errors.values()))
            return render(request, 'pages/sign_up.html', {'form':form, 'messages':messages})
           
    else:
        form = CustomUserCreationForm()
        return render(request, 'pages/sign_up.html', {'form':form})


def settings(request):
    return render(request, 'pages/settings/index.html')

def user_data(request):
    return render(request, 'pages/settings/data.html')


def workers(request):
    return render(request, 'pages/workers.html')