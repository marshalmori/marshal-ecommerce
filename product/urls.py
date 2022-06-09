from django.urls import path

from product import views

urlpatterns = [
    path('detail/', views.product_detail, name='detail'),
]
