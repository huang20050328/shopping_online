from django.shortcuts import render, redirect, HttpResponse
from app01.models import user_info
import hashlib

def Encode(a):
    md = hashlib.md5(a.encode())
    return md.hexdigest()

def login(request):
    return render(request, 'login.html')

def verifying(request):
    pass

def registration(request):
    return render(request, 'registration.html')

def registration_verifying(request):
    pass