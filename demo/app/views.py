from ast import Return
from wsgiref.util import request_uri
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout
from . models import Brand, Category, Product, Memory, ProductColor, ProductColorSize, Cart, Order, OrderProduct, Color
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


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





# Admin panel

def admin_product(request):
    products = Product.objects.order_by('-id')
    return render(request, 'pages/admin/product.html', {'products':products})


def admin_product_detail(request, id):
    product = Product.objects.get(id=id)
    sizes = Memory.objects.order_by('-id')
    return render(request, 'pages/admin/product-detail.html', {'product':product, 'sizes':sizes})




@csrf_exempt
def admin_product_detail_memory_edit(request):
    id = request.POST.get('id')
    price = request.POST.get('price')

    productColorSize = ProductColorSize.objects.get(id=id)

    productColorSize.price = price
    productColorSize.save()

    return HttpResponse(price)
      


def admin_product_detail_memory_more(request, id, productId):
    if request.method == 'POST':
    
        price = request.POST.getlist('price')
        memory = request.POST.getlist('memory')

     
        productColor = ProductColor.objects.get(id=id)

        for item in range(0, len(price)):
            product = ProductColorSize()
            product.price = price[item]
            size = Memory.objects.get(id=memory[item])
            product.memory = size
            product.productColor = productColor

            product.save()

        return redirect(reverse('admin_product_detail', kwargs={'id':productId}))
        

def admin_product_detail_memory_create(request,id, productId):
    if request.method == "POST":
        sizeId = request.POST.get('size')

        productColor = ProductColor.objects.get(id=id)
        price = request.POST.get('price')
        size = Memory.objects.get(id=sizeId)

        productColorSize = ProductColorSize()
        productColorSize.price = price
        productColorSize.memory = size
        productColorSize.productColor = productColor
        productColorSize.save()

        return redirect(reverse('admin_product_detail', kwargs={'id':productId}))
        

      

        

        


def product_create(request):
    if request.method == 'POST':
        
        category = request.POST.get('category')  
        brand = request.POST.get('brand')  
        title = request.POST.get('title')  
        year = request.POST.get('year')  
        text = request.POST.get('text')  

        colors_id = [int(item) for item in request.POST.getlist('colors[]')]

        product = Product()
        product.title = title
        product.year = year
        product.text = text
        
        product.category = Category.objects.get(id=category)
        product.brand = Brand.objects.get(id=brand)
        if request.POST.get('image') == '':
            product.save()
        else:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            product.image = filename
            product.save()
        

        for color in colors_id:
            productColor = ProductColor()
            productColor.color = Color.objects.get(id=color)
            productColor.product = product
            productColor.save()

        return redirect('admin_product')
      
    else:
        brands = Brand.objects.order_by('-id')
        categories = Category.objects.order_by('-id')
        colors = Color.objects.order_by('-id')
        return render(request, 'pages/admin/create-product.html',{'brands':brands,'categories':categories, 'colors':colors })