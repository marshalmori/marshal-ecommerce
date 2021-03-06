
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(
        template_name='core/pages/login.html'),
        name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('myaccount/edit/', views.edit_myaccount, name='edit_myaccount'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
