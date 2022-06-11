from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]
