from django.db import models
from django.contrib.auth.models import User
from ecommerce_api.models import RatingsModel

class MerchantProfile(models.Model):
    owner = models.ForeignKey(User, related_name='merchantProfile', on_delete=models.CASCADE,null=True)
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phoneNumber = models.CharField(max_length=100, blank=True)
    walletBalance = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.0)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class ProductModel(models.Model):
    owner = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE, null= True)
    productId= models.TextField(blank=True)
    productName = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=11, blank=True, decimal_places=2, default=0.00)
    quantity = models.IntegerField(blank=True, default=0)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    # rating= models.ForeignKey(RatingsModel,on_delete=models.CASCADE,related_name='product_ratings',null=True)
    # rating=models.ManyToOneRel(RatingsModel,to='RatingsModel',field_name='rating_value',on_delete=models.CASCADE,related_name='product_ratings')

    def __str__(self):
        return self.productName
    
    

