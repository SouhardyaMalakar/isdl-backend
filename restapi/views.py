from datetime import datetime, timedelta
from multiprocessing import AuthenticationError
from tkinter import N
import jwt
from django.shortcuts import render
from django.http import JsonResponse
from django.http.request import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed

from restapi.models import User
from .serializers import USerLoginSerializer, UserSerializer

def api_home(request ,*args, **kwargs):
    return JsonResponse({"Message" :"this is inside"})

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer=USerLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    email=request.data['email']
    password=request.data['password']
    user=User.objects.filter(email=email).first()
    if user==None:
        raise AuthenticationFailed('User not found')
    if user.check_password(password)==False:
        raise AuthenticationFailed("incorrect password")
    payload={
        'id':user.id,  # type: ignore
        'name':user.name,
        'email':user.email,
        'exp':datetime.utcnow()+timedelta(minutes=30),
        'iat':datetime.utcnow()       
    }

    token=jwt.encode(payload=payload,key='secret',algorithm='HS256')
    response=Response()
    response.set_cookie(key='jwt',value=token,httponly=True)
    decode=jwt.decode(token,'secret',algorithms=['HS256'])
    response.data={'jwt':token}
    return response


def Decode(token):
    try:
        decode=jwt.decode(token,'secret',algorithms=['HS256'])
        return decode
    except:
        return None

def authuser(request): #returns user 
    payload=Decode(request.query_params.get('jwt',"lol"))
    if payload==None:
        return None #cannot auth user
    user=User.objects.get(pk=payload['id'])
    if user:
        return user
    else:
        return None

def authadmin(request):
    payload=Decode(request.query_params.get('jwt',"lol"))
    if payload==None:
        return None #cannot auth user
    user=User.objects.get(pk=payload['id'])
    if user and user.isAdmin:
        return user
    else:
        return None
    
#lol2
@api_view(['GET'])
def userView(request):
    user=authuser(request)
    if user:
        serializer=USerLoginSerializer(user)
        r=Response()
        r.data=serializer.data
        return r
    else:
        raise AuthenticationError("Not Authenticated")

@api_view(['POST'])
def logout(request):
    response=Response()
    response.delete_cookie('jwt')
    response.data={"message":"success"}
    return response



