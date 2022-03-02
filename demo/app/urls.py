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


    path('page/settings/index.html', views.settings, name='settings')
]
