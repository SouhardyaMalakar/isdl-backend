from datetime import datetime, timedelta
import jwt
import email
import imp
from re import T
from tkinter import N
from django.shortcuts import render
from django.http import JsonResponse
from django.http.request import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed

from restapi.models import User
from .serializers import USerLoginSerializer

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
        'name':user.email,
        'exp':datetime.utcnow()+timedelta(minutes=30),
        'iat':datetime.utcnow()       
    }

    token=jwt.encode(payload=payload,key='secret',algorithm='HS256')
    response=Response()
    response.set_cookie(key='jwt',value=token,httponly=True)
    decode=jwt.decode(token,'secret',algorithms=['HS256'])
    response.data={'jwt':token}
    return response



@api_view(['GET'])
def userView(request):
    token=request.COOKIES.get('jwt')
    if token==None:
        raise AuthenticationFailed("Unauthenticated")
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except:
        raise AuthenticationFailed("Unauthenticated")
    user=User.objects.get(pk=payload['id'])
    serializer=USerLoginSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def logout(request):
    response=Response()
    response.delete_cookie('jwt')
    response.data={"message":"success"}
    return response



