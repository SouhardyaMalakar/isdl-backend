from django.shortcuts import render
from django.http import JsonResponse

def api_home(request ,*args, **kwargs):
    return JsonResponse({"Message" :"this is inside"})

# Create your views here.
