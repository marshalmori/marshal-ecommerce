from django.db.models import Q
from django.shortcuts import render
from product.models import Category, Product


def create_prod_cat(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }


def signup(request):
    return render(request, 'core/pages/signup.html')


def home(request):
    return render(request, 'core/pages/home.html', create_prod_cat(request))


def shop(request):
    return render(request, 'core/pages/shop.html', create_prod_cat(request))
