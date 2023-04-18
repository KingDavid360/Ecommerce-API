from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserProfile(models.Model):
    owner = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE,null=True)
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phoneNumber = models.CharField(max_length=100, blank=True)
    walletBalance = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.0)
    dateCreated = models.DateField(default= date.today)

    def __str__(self):
        return self.email

class CartModel(models.Model):
    owner = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE, null= True)
    productId= models.TextField(blank=True)
    productName = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.00)
    quantity = models.IntegerField(blank=True, default=0)
    # ratings = models.DecimalField(max_digits=5, blank=True, decimal_places=1, default=0.0)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)

    def __str__(self):
        return self.productName
    
class RatingsModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user_ratings')
    rating_value = models.DecimalField(max_digits=5, blank=True, decimal_places=1, default=0.0)
    productId= models.TextField(blank=True)

    def __str__(self):
        return self.productId
    
class CheckoutModel(models.Model):
    owner = models.ForeignKey(User, related_name='checkout', on_delete=models.CASCADE, null= True)
    productId= models.TextField(blank=True)
    productName = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.00)
    quantity = models.IntegerField(blank=True, default=1)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    total_cost= models.DecimalField(max_digits=12, blank=True, decimal_places=2, default=0.00)
    final_cost= models.DecimalField(max_digits=12, blank=True, decimal_places=2, default=0.00)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.productName
