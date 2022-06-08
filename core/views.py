from django.shortcuts import render


def home(request):
    return render(request, 'global/base.html')
