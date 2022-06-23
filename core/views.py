from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from product.models import Category, Product

from .forms import SignUpForm


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'core/pages/signup.html', {'form': form})


@login_required
def myaccount(request):
    return render(request, 'core/pages/myaccount.html')


@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()
        return redirect('myaccount')
    return render(request, 'core/pages/edit_myaccount.html')

# def login_(request):
#     return render(request, 'core/pages/login.html')


def home(request):
    return render(request, 'core/pages/home.html', create_prod_cat(request))


def shop(request):
    return render(request, 'core/pages/shop.html', create_prod_cat(request))
