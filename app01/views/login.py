from django.shortcuts import render, redirect, HttpResponse
from app01.models import UserInfo
from app01.views import mainmenu
import hashlib
import re
import jwt
import datetime
import requests
from django.http import JsonResponse
from utils import app_jwt


# def get_token(username):
#     """
#     登录成功后获取token
#     """
#
#     SECRET_KEY = 'jianguolanglang'
#
#     payload = {
#         'user_name': username,
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=20)
#     }
#
#     token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#     return token


def Encode(a):
    md = hashlib.md5(a.encode())
    return md.hexdigest()


def username_rule(text):
    """
    注册
    用户名长度要求5-20位
    不可包含特殊符号
    至少有一个数字和字母
    """
    if len(text) < 5:
        return '用户名至少拥有5个字符'

    if len(text) > 20:
        return '用户名最多拥有20个字符'

    pattern1 = re.compile(r'[^a-zA-Z0-9]+')
    pattern2 = re.compile(r'[^a-zA-Z]+')
    pattern3 = re.compile(r'[^0-9]+')

    result1 = re.search(pattern1, text)
    print(result1)
    if result1:
        return '用户名不可以包含特殊符号'

    result2 = re.search(pattern2, text)
    print(result2)
    if not result2:
        return '用户名至少包含一个数字'

    result3 = re.search(pattern3, text)
    print(result3)
    if not result3:
        return '用户名至少包含一个字母'

    if UserInfo.objects.filter(username=text).exists():
        return '用户名已存在'

    return False


def password_rule(text):
    """
    注册
    密码长度要求5-20位
    不可包含特殊符号
    至少有一个数字和字母
    """
    if len(text) < 5:
        return '密码至少拥有5个字符'

    if len(text) > 20:
        return '密码最多拥有20个字符'

    pattern1 = re.compile(r'[^a-zA-Z0-9]+')
    pattern2 = re.compile(r'[^a-zA-Z]+')
    pattern3 = re.compile(r'[^0-9]+')

    result1 = re.search(pattern1, text)
    if result1:
        return '密码不可以包含特殊符号'

    result2 = re.search(pattern2, text)
    if not result2:
        return '密码至少包含一个数字'

    result3 = re.search(pattern3, text)
    if not result3:
        return '密码至少包含一个字母'

    return True


def login(request):
    return render(request, 'login.html')


def verifying(request):
    """
    登录验证用户名和密码
    """
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST['user']
    password = request.POST['pwd']

    user = UserInfo.objects.filter(username=username).first()
    if user:
        if Encode(password) == user.password:
            user_id = user.id
            payload = {
                'user_id': user_id,
            }
            token = app_jwt.jwt_encode_handler(payload)
            print(token)
            return JsonResponse({"code": 0, "token": token})
    return JsonResponse({"code": 1, "msg": "用户名或密码错误", "user": username, "pwd": password})


def registration(request):
    return render(request, 'registration.html', {'user': "", 'pwd': ""})


def registration_verifying(request):
    """
    注册验证用户名与密码是否合规
    """
    if request.method == "GET":
        return render(request, "registration.html", {'user': "", 'pwd': ""})
    username = request.POST['user']
    password = request.POST['pwd']
    con_password = request.POST['conpwd']
    a = username_rule(username)
    if not a:
        b = password_rule(password)
        if b:
            if con_password == password:
                UserInfo.objects.create()
                id = UserInfo.objects.last().id
                UserInfo.objects.filter(id=id).update(name="用户" + str(id), username=username,
                                                      password=Encode(password))
                return render(request, 'login.html', {'code': 2, 'msg': '注册成功'})
            else:
                return render(request, 'registration.html',
                              {'msg': "两次密码不匹配", 'user': username, 'pwd': password})
        else:
            return render(request, 'registration.html', {'msg': b, 'user': username, 'pwd': password})

    else:
        return render(request, 'registration.html', {'msg': a, 'user': username, 'pwd': password})


def change_pwd(request):
    pass


def change_pwd_verifying(request):
    pass
