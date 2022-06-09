from django.shortcuts import render
from product.models import Category, Product


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/pages/home.html',
                  context={'products': products, 'categories': categories})


def shop(request):
    products = Product.objects.all()
    return render(request, 'core/pages/shop.html',
                  context={'products': products})
