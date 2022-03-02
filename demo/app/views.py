from ast import Return
from wsgiref.util import request_uri
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout
from . models import Product, ProductColor, ProductColorSize, Cart, Order, OrderProduct
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'pages/index.html', {'products':products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    productColors = product.productcolor_set.all()
   
    
    return render(request, 'pages/product-detail.html', {'productColors':productColors, 'product':product})


def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'pages/cart.html', {'cart':cart})


@csrf_exempt
def cartPlus(request):
    cart_id = request.POST.get('cart_id')

    cart = Cart.objects.get(id=cart_id)

    cart.quantity += 1
    cart.save()
    return HttpResponse('ok')


@csrf_exempt
def cartMinus(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')
    
    cart = Cart.objects.get(id=cart_id)

    if quantity == '1':
        cart.delete()
        return HttpResponse('removed')
    else:
        cart.quantity -= 1
        cart.save()
        return HttpResponse('ok')
        


@csrf_exempt
def addToCart(request):
    user = request.user
    data = request.POST.get('product')
    product = ProductColorSize.objects.get(id=data)

    if Cart.objects.filter(user=user).filter(product=product).exists():
        cart = Cart.objects.filter(user=user).get(product=product)
        
        cart.quantity = cart.quantity + 1
        cart.save()
        return HttpResponse('exist')
    else:
        cart = Cart()
        cart.product = product
        cart.quantity = 1
        cart.user = user
        cart.save()
        return HttpResponse('new')

    


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


def new_order(request):
    if request.method == "POST":
        total = request.POST.get('total')
        if Cart.objects.filter(user = request.user).exists():
            order = Order()
            order.user = request.user
            order.total = total
            order.save()
            for item in Cart.objects.filter(user = request.user):
                orderProduct = OrderProduct()
                orderProduct.order = order
                orderProduct.product = item.product
                orderProduct.product_count = item.quantity
                orderProduct.save()

        return redirect(reverse('order_detail', kwargs={'id':order.id}))


     
        

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'pages/order.html', {'order':order})
    

   


def settings(request):
    return render(request, 'pages/settings/index.html')


def user_data(request):
    return render(request, 'pages/settings/data.html')


def workers(request):
    return render(request, 'pages/workers.html')




    