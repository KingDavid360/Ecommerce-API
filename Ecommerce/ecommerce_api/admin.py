from django.contrib import admin
from .models import UserProfile, CartModel, RatingsModel, CheckoutModel

admin.site.register(UserProfile)
admin.site.register(CartModel)
admin.site.register(RatingsModel)
admin.site.register(CheckoutModel)