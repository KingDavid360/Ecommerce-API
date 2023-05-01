from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.db import IntegrityError 
from django.http import JsonResponse
from django.contrib.auth.models import User 
from .models import UserProfile
from django.contrib.auth import login, authenticate
import traceback
from merchants.models import ProductModel,RatingsModel
from .models import CartModel, CheckoutModel
from .serializer import ProductSerializer, CartSerializer, UserSerializer

@api_view(['post'])
@csrf_exempt
def registerUser(request):
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
        userProfile = UserProfile.objects.create(
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
        res = {"status": 400, "message": "user already exist"}
        return JsonResponse(res, status=400, safe=False)
    except:
        traceback.print_exc()
        res = {"status": 500, "message": "Server error"}
        return JsonResponse(res, status=500, safe=False)
    
@api_view(['Get'])
@csrf_exempt
def fetchCustomer(request):
    if request.user.is_authenticated:
        try:
            get_user = UserProfile.objects.all()
            serializer = UserSerializer(get_user, many= True)
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
def loginUser(request):
    email = request.data['email']
    password = request.data['password']
    try:
        getUser = User.objects.get(username = email)
        user = authenticate(username=getUser, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user = user)
                res = {'status': 200, 'token': token.key}
                return JsonResponse(res, status= 200, safe=False)
            except:
                traceback.print_exc()
                res = {"status": 500, "message": "Server error"}
                return JsonResponse(res, status=500, safe=False)
        else: 
            traceback.print_exc()
            res = {"status": 400, "message": "user not found"}
            return JsonResponse(res, status=400, safe=False)
    except:
        traceback.print_exc()
        res = {"status": 500, "message": "Enter all fields correctly"}
        return JsonResponse(res, status=500, safe=False)
    
@api_view(['Get'])
@csrf_exempt
def fetchProduct(request):
    if request.user.is_authenticated:
        try:
            getProduct = ProductModel.objects.all()
            serializer = ProductSerializer(getProduct, many= True)
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
def addToCart(request):
    productId = request.data['productId']

    if request.user.is_authenticated:
        try:
            product = ProductModel.objects.get(productId=productId)
            profile = UserProfile.objects.get(owner=request.user)
            cart = CartModel.objects.create(
                owner=request.user,
                productId=productId,
                productName=product.productName,
                price=product.price,
                quantity=product.quantity,
                description=product.description,
                image=product.image,
            )
            cart.save()
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

@api_view(['Get'])
@csrf_exempt
def fetchCart(request):
    if request.user.is_authenticated:
        try:
            getCart = CartModel.objects.filter(owner=request.user)
            serializer = CartSerializer(getCart, many=True)
            res = {"status": 200, "message": "successful", "data": serializer.data}
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
def rateProduct(request):
    user=request.user
    productId=request.data['productId']
    rating_value=request.data['rating']
    if user.is_authenticated:
        try:
            rating= RatingsModel.objects.get(productId=productId)
            if user == rating.user:
                 res = {"status": 400, "message": "User already rated this product"} 
                 return JsonResponse(res, status=200, safe=False)
            else:
                rating.user=user
                rating.rating_value=rating_value
                rating.save()
                res = {"status": 200, "message": "Successful"} 
                return JsonResponse(res, status=200, safe=False)
        except:
            traceback.print_exc()
            res = {"status": 500, "message": "server error"}
            return JsonResponse(res, status=500, safe=False)
    else:
        traceback.print_exc()
        res={"status":400, "message": "User not authenticated"}
        return JsonResponse(res, status=400, safe=False)


@api_view(['post'])
@csrf_exempt
def checkout(request):
    productId=request.data['productId']
    quantity=request.data['quantity']
    address=request.data['address']
    total_cost=request.data['total_cost']
    final_cost=request.data['final_cost']
    user=request.user
    if user.is_authenticated:
        try:
            product = ProductModel.objects.get(productId=productId)
            checkout=CheckoutModel.objects.create(
                owner=user,
                productId=productId,
                productName=product.productName,
                price=product.price,
                quantity=quantity,
                description=product.description,
                image=product.image,
                address=address,
                total_cost=total_cost,
                final_cost=final_cost
            )  
            checkout.save
            res={"status":200, "message":"Successful"}
            return JsonResponse(res, status=200, safe=False)
        except:
            traceback.print_exc()
            res={"status":400, "message": "Server error"}
            return JsonResponse(res, status=400, safe=False)
    else:
        traceback.print_exc()
        res={"status":400, "message": "Server error"}
        return JsonResponse(res, status=400, safe=False)