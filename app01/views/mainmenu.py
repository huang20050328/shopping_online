from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from app01.models import user_info
import jwt
import datetime
from app01.views import login
import requests


def mainmenu(request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            decoded_payload = jwt.decode(token, 'jianguolanglang', algorithms=['HS256'])
            user = user_info.objects.filter(username=decoded_payload['user_name']).first()
            return render(request, 'mainmenu.html',{'msg':'登录成功', 'user_id': user.id})
        except jwt.ExpiredSignatureError:
            return render(request, 'mainmenu.html', {'msg':'登录超时'})
        except jwt.InvalidTokenError:
            return render(request, 'mainmenu.html', {'msg':'未登录'})
