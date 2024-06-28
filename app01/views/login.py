from django.shortcuts import render, redirect, HttpResponse
from app01.models import user_info
import hashlib
import re

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
    pass

def registration(request):
    return render(request, 'registration.html')

def registration_verifying(request):
    if request.method == "GET":
        return render(request, "registration.html")
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
                return render(request, 'registration.html', {'msg': "两次密码不匹配"})
        else:
            return render(request, 'registration.html', {'msg': b})

    else:
        return render(request, 'registration.html', {'msg': a})
