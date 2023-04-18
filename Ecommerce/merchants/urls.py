from django.urls import path
from . import views

urlpatterns =[
    path('register-merchant', views.registerMerchant),
    path('create-product', views.createProduct),
]