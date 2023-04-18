from django.urls import path
from . import views

urlpatterns =[
    path('register-customer', views.registerUser),
    path('login-user', views.loginUser),
    path('fetch-product', views.fetchProduct),
    path('add-cart', views.addToCart),
    path('fetch-cart', views.fetchCart),
    path('rate-product', views.rateProduct),
    path('checkout', views.checkout),
]