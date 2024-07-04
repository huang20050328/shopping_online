from django.shortcuts import render, redirect, HttpResponse
from app01.models import user_info
from app01.views import mainmenu
import hashlib
import re
import jwt
import datetime
import requests
from django.http import JsonResponse

def get_token(username):
    SECRET_KEY = 'jianguolanglang'

    payload = {
        'user_name': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=20)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def Encode(a):
    md = hashlib.md5(a.encode())
    return md.hexdigest()

def usernamerule(text):
    if len(text) < 5:
        return '用户名至少拥有5个字符'

    if len(text)> 20:
        return '用户名最多拥有20个字符'

    pattern1 = re.compile(r'[^a-zA-Z0-9]+')
    pattern2 = re.compile(r'[^a-zA-Z]+')
    pattern3 = re.compile(r'[^0-9]+')

    result1 = re.search(pattern1, text)
    print(result1)
    if result1 != None:
        return '用户名不可以包含特殊符号'

    result2 = re.search(pattern2, text)
    print(result2)
    if result2 == None:
        return '用户名至少包含一个数字'

    result3 = re.search(pattern3, text)
    print(result3)
    if result3 == None:
        return '用户名至少包含一个字母'

    if user_info.objects.filter(username=text).exists():
        return '用户名已存在'

    return True


def passwordrule(text):
    if len(text) < 5:
        return '密码至少拥有5个字符'

    if len(text) > 20:
        return '密码最多拥有20个字符'

    pattern1 = re.compile(r'[^a-zA-Z0-9]+')
    pattern2 = re.compile(r'[^a-zA-Z]+')
    pattern3 = re.compile(r'[^0-9]+')

    result1 = re.search(pattern1, text)
    if result1 != None:
        return '密码不可以包含特殊符号'

    result2 = re.search(pattern2, text)
    if result2 == None:
        return '密码至少包含一个数字'

    result3 = re.search(pattern3, text)
    if result3 == None:
        return '密码至少包含一个字母'

    return True

def login(request):
    return render(request, 'login.html')

def verifying(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST['user']
    password = request.POST['pwd']

    user = user_info.objects.filter(username=username).first()
    if user != None:
        if Encode(password) == user.password:
            token = get_token(username)
            str_token = str(token, encoding='utf-8')
            return JsonResponse({"code":0, "token": str_token})
    return JsonResponse({"code":1 , "msg":"用户名或密码错误", "user": username, "pwd": password})


def registration(request):
    return render(request, 'registration.html', {'user': "", 'pwd': ""})

def registration_verifying(request):
    if request.method == "GET":
        return render(request, "registration.html", {'user': "", 'pwd': ""})
    username = request.POST['user']
    password = request.POST['pwd']
    conpassword = request.POST['conpwd']
    a = usernamerule(username)
    if a == True:
        b = passwordrule(password)
        if b == True:
            if conpassword == password:
                user_info.objects.create()
                id = user_info.objects.last().id
                user_info.objects.filter(id=id).update(name="用户" + str(id), username=username, password=Encode(password))
                return render(request, 'login.html', {'msg': '注册成功'})
            else:
                return render(request, 'registration.html', {'msg': "两次密码不匹配", 'user': username, 'pwd': password})
        else:
            return render(request, 'registration.html', {'msg': b, 'user': username, 'pwd': password})

    else:
        return render(request, 'registration.html', {'msg': a, 'user': username, 'pwd': password})

