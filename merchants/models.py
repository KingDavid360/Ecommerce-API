from django.db import models
from django.contrib.auth.models import User
from datetime import date

class MerchantProfile(models.Model):
    owner = models.ForeignKey(User, related_name='merchantProfile', on_delete=models.CASCADE,null=True)
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phoneNumber = models.CharField(max_length=100, blank=True)
    walletBalance = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.0)
    dateCreated = models.DateField(auto_now_add=True)

class ProductModel(models.Model):
    owner = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE, null= True)
    productName = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.00)
    quantity = models.IntegerField(blank=True, default=0)
    ratings = models.DecimalField(max_digits=5, blank=True, decimal_places=1, default=0.0)
    description = models.TextField(blank=True)
    
    

