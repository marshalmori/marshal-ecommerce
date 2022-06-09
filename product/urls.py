from django.urls import path

from product import views

urlpatterns = [
    path('detail/<int:pk>/', views.product_detail, name='detail'),
]
