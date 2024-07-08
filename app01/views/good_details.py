from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from app01.views import mainmenu
from app01.models import goods_info
from app01.models import cart_info
from django.http import JsonResponse
from django.forms.models import model_to_dict
from utils import app_jwt
import os
from django.conf import settings


@app_jwt.decorator_login_require
def state(request):
    return JsonResponse({'code': 0, 'user_id': request.user.id})


def good_details(request):
    """
    返回商品详情页面
    """
    good_id = request.GET.get('good_id')
    return render(request, "good_details.html", {'good_id': good_id})


def good(request):
    """
    获取对应商品的信息列表
    """
    good_id = request.GET.get('good_id')
    good = goods_info.objects.filter(id=good_id).first()
    good_info = model_to_dict(goods_info.objects.get(id=good_id))
    good_info['image'] = os.path.join(settings.MEDIA_URL, 'img', good.image)
    return JsonResponse(good_info)


def add_to_cart(request):
    """
    添加到购物车
    """
    good_id = request.POST.get('good_id')
    user_id = request.POST.get('user_id')
    count = request.POST.get('count')
    cart_info.objects.create(good_id=good_id, user_id=user_id, count=count)
    return HttpResponse("添加成功")
