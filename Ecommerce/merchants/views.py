from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.db import IntegrityError 
from django.http import JsonResponse
from django.contrib.auth.models import User 
from .models import MerchantProfile, ProductModel
from django.contrib.auth import login
import traceback
import uuid
import cloudinary.uploader
from ecommerce_api.models import RatingsModel, UserProfile
from .serializer import MerchantSerializer

@api_view(['post'])
@csrf_exempt
def registerMerchant(request):
    firstName = request.data['firstName']
    lastName = request.data['lastName']
    phoneNumber = request.data['phoneNumber']
    email = request.data['email']
    password = request.data['password']
    
    try:
        user = User.objects.create_user(
            first_name = firstName,
            last_name = lastName,
            email= email,
            password= password,  
            username= email,  
        )
        user.save()
        userProfile = MerchantProfile.objects.create(
            owner = user,
            firstName = firstName,
            lastName = lastName,
            email= email,
            phoneNumber = phoneNumber,
        )
        userProfile.save()
        token = Token.objects.create(
            user = user
        )
        login(request,user)
        res = {'status': 200, 'token': token.key}
        return JsonResponse(res, status= 200, safe= False)
    except IntegrityError:
        traceback.print_exc()
        res = {"status": 400, "message": "Incorrect input"}
        return JsonResponse(res, status=400, safe=False)
    except:
        traceback.print_exc()
        res = {"status": 500, "message": "Server error"}
        return JsonResponse(res, status=500, safe=False)
    

@api_view(['Get'])
@csrf_exempt
def fetchMerchant(request):
    if request.user.is_authenticated:
        try:
            get_user = MerchantProfile.objects.all()
            serializer = MerchantSerializer(get_user, many= True)
            res = {"status": 200, "message": "successful", 'data': serializer.data}
            return JsonResponse(res, status=200, safe=False)
        except:
            traceback.print_exc()
            res = {"status": 500, "message": "Server error"}
            return JsonResponse(res, status=500, safe=False)
    else:
        traceback.print_exc()
        res = {"status": 400, "message": "user not authenticated"}
        return JsonResponse(res, status=400, safe=False)
    

@api_view(['post'])
@csrf_exempt
def createProduct(request):
    productName = request.data['productName']
    price = request.data['price']
    quantity = request.data['quantity']
    description = request.data['description']
    # rating_value= request.data['rating_value']
    if request.user.is_authenticated:
        try:
            productId = f"{productName}{str(uuid.uuid4())[:10]}"
            product = ProductModel.objects.create(
                productId = productId,
                owner = request.user,
                productName = productName,
                price = price,
                quantity = quantity,
                description = description,
                image = upload_product_image(request),
            )
            product.save()
            rating = RatingsModel.objects.create(
                # user=UserProfile.objects.get(owner=request.user),
                productId=productId,
                # rating_value = rating_value
            )
            rating.save
            res = {"status": 200, "message": "Successful"} 
            return JsonResponse(res, status=200, safe=False)
        except:
            traceback.print_exc()
            res = {"status": 500, "message": "server error"}
            return JsonResponse(res, status=500, safe=False)
    else:
        traceback.print_exc()
        res = {"status": 400, "message": "User not authenticated"}
        return JsonResponse(res, status=400, safe=False)
    
def upload_product_image(request):
   try:
      image=request.data['image']
      upload_image = cloudinary.uploader.upload(image)
      print(upload_image)
      return upload_image["url"]
   except:
       traceback.print_exc()

