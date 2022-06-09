from django.shortcuts import render
from product.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'core/pages/home.html',
                  context={'products': products, })


def shop(request):
    products = Product.objects.all()
    return render(request, 'core/pages/shop.html',
                  context={'products': products})
