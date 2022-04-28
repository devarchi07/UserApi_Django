from django.shortcuts import render,HttpResponse
from django.http import response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import User,Seller
from .searializers import Userserializers,Sellerserializers
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def viewuser(request):
    obj1=User.objects.all()
    serializer=Userserializers(obj1,many=True)
    return Response(serializer.data)
            

@api_view(['GET'])
def viewseller(request):
    obj1=Seller.objects.all()
    serializer=Sellerserializers(obj1,many=True)
    return Response(serializer.data)
            

@api_view(['POST'])
def adduser(request):
    serializer=Userserializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def addseller(request):
    serializer=Sellerserializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['GET'])
def deluser(request, pk):
    object=User.objects.get(user_id=pk)
    User.delete()

    return Response("user deleted sucessfully")


@api_view(['GET'])
def delseller(request, pk):
    object=Seller.objects.get(user_id=pk)
    Seller.delete()

    return Response("user deleted sucessfully")


   
        
    return Response(serializer.data)



    
            

        







            
