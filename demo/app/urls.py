from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('sign-out', views.sign_out, name='sign_out'),

    path('product/<int:id>', views.product_detail, name='product_detail'),

    path('cart/', views.cart, name='cart'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('cartPlus/', views.cartPlus, name='cartPlus'),
    path('cartMinus/', views.cartMinus, name='cartMinus'),

    path('new-order/', views.new_order, name='new_order'),
    path('order-detail/<int:id>/', views.order_detail, name='order_detail'),


    path('settings/index.html', views.settings, name='settings'),


    # Admin panel
    path('user/product', views.admin_product, name='admin_product'),
    path('user/product/<int:id>', views.admin_product_detail, name='admin_product_detail'),
    # True
    path('user/product-memory-edit/>', views.admin_product_detail_memory_edit, name='admin_product_detail_memory_edit'),
    path('user/create/productColor/<int:id>/', views.productColor_create, name='productColor_create'),





   


    path('user/create/product', views.product_create, name='product_create')
]
