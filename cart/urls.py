from django.urls import path

from cart import views

urlpatterns = [
    path('add_to_cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
    path('', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('hx_menu_cart/', views.hx_menu_cart, name='hx_menu_cart'),
]
