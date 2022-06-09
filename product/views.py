from django.shortcuts import render

from product.models import Product


def product_detail(request, pk):
    product_detail = Product.objects.filter(pk=pk).order_by('-pk').first()
    return render(request, 'product/product_detail.html', context={
        'product_detail': product_detail,
    })
