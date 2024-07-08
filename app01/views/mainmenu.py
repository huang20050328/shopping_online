import json

from django.forms import model_to_dict
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from app01.models import user_info
from app01.models import goods_info
import jwt
import datetime
from app01.views import login
import requests
from django.http import JsonResponse
import random


def state(request):
    try:
        token = request.META.get("HTTP_AUTHORIZATION")
        decoded_payload = jwt.decode(token, 'jianguolanglang', algorithms=['HS256'])
        user = user_info.objects.filter(username=decoded_payload['user_name']).first()
        return JsonResponse({'code': 0, 'user_id': user.id})
    except jwt.ExpiredSignatureError:
        return JsonResponse({'code': 1})
    except jwt.InvalidTokenError:
        return JsonResponse({'code': 1})


def mainmenu(request):
    return render(request, 'mainmenu.html')


def good_list(request):
    """
    首页商品列表接口
    """
    query = goods_info.objects.all()
    data = [dict(model_to_dict(i), **{
        'image': 111
    }) for i in query]
    print(data)
    return JsonResponse(data,)
    # Rng = goods_info.objects.last()
    # rng = Rng.id
    # i = 0
    # list = []
    # List = ()
    #
    # while i <= 20:
    #     goodid = random.randint(1,rng)
    #     good = goods_info.objects.get(id=goodid)
    #     if good != None:
    #         try:
    #             List.__add__(goodid)
    #             list.__add__({'good_id':good.id, 'good_name':good.name, 'good_topic':good.topic, 'good_price':good.price, 'good_image':good.image, 'store_name':good.store.name})
    #             i = i + 1
    #         except:
    #             pass
    # return JsonResponse({'good1': list[0], 'good2': list[1], 'good3': list[2], 'good4': list[3], 'good5': list[4], 'good6': list[5], 'good7': list[6], 'good8': list[7], 'good9': list[8], 'good10': list[9], 'good11': list[10], 'good12': list[11], 'good13': list[12], 'good14': list[13], 'good15': list[14], 'good16': list[15], 'good17': list[16], 'good18': list[17], 'good19': list[18], 'good20': list[19]})
