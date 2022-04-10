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
    path('user/product-image/<int:id>/', views.admin_product_image_edit, name='admin_product_image_edit'),

    path('user/product/<int:id>', views.admin_product_detail, name='admin_product_detail'),
    path('user/create/product', views.product_create, name='product_create'),
    # Product Color Size
    path('user/product-memory-edit/>', views.admin_product_detail_memory_edit, name='admin_product_detail_memory_edit'),
    path('user/create/productColor/<int:id>/', views.productColor_create, name='productColor_create'),
    path('user/delete/productColor/<int:id>/', views.productColor_delete, name='productColor_delete'),
    # Product Color Size Gallery
    path('user/gallery/productColor/<int:id>/', views.productColor_gallery, name='productColor_gallery'),
    path('user/gallery/productColor/<int:id>/create', views.productColor_gallery_create, name='productColor_gallery_create'),
    path('user/gallery/productColor/remove', views.productColor_gallery_remove, name='productColor_gallery_remove'),

    # Storage
    path('storage/', views.storage, name='storage'),
    path('storage-detail/<int:id>/', views.storage_detail, name='storage_detail'),
    path('storage/<int:id>/', views.storage_reload, name='storage_reload')




    
]
