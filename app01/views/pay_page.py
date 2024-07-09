import os

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework_jwt.serializers import User

from app01.models import GoodsInfo, UserInfo, OrderInfo, CartInfo
from shopping import settings


def pay_page(request):
    """
    返回订单结算的页面
    """
    return render(request, 'pay_page.html')


def from_cart(request):
    """
    购物车结算的商品信息接口
    """
    if request.method == 'POST':
        cart_id = request.POST['cart_id']
        cart = CartInfo.objects.get(id=cart_id)
        good_id = cart.good_id
        count = cart.count
        good = GoodsInfo.objects.filter(id=good_id).first()
        good_info = dict(model_to_dict(good), **{'image': os.path.join(settings.MEDIA_URL, 'img/', good.image), 'count': count})
            # good_info['count']: count
        return JsonResponse(good_info)
    return JsonResponse({'code': 1})


def from_details(request):
    """
    商品详情页直接购买的商品信息接口
    """
    if request.method == 'POST':
        good = GoodsInfo.objects.filter(id=request.POST['good_id']).first()
        if good:
            good_info = dict(model_to_dict(good), **{'image': os.path.join(settings.MEDIA_URL, 'img/', good.image),
                                                     'count': request.POST['count']})
            return JsonResponse(good_info)
        return HttpResponse('商品已下架')
    return JsonResponse({'code': 1})


def from_order(request):
    """
    订单页再来一单的商品信息接口
    """
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = OrderInfo.objects.get(id=order_id)
        count = order.count
        good = GoodsInfo.objects.filter(id=order.good_id).first()
        if good:
            good_info = dict(model_to_dict(good),
                             **{'image': os.path.join(settings.MEDIA_URL, 'img/', good.image), 'count': count})
            # good_info['count']: count
            return JsonResponse(good_info)
        return HttpResponse('商品已下架')
    return JsonResponse({'code': 1})


def submit(request):
    if request.method == 'POST':
        good_id = request.POST['good_id']
        count = request.POST['count']
        user_id = request.POST['user_id']
        user_address = request.POST['user_address']
        good = GoodsInfo.objects.filter(id=good_id).first()
        user = UserInfo.objects.filter(id=user_id).first()
        price = good.price * int(count)
        OrderInfo.objects.create(good_id=good_id, user_id=user_id, user_name=user.name, user_address=user_address,
                                 user_phone=user.phonenum, good_name=good.name, good_image=good.image,
                                 good_price=good.price, count=count, price=price)
        return HttpResponse('购买成功')
    return JsonResponse({'code': 1})
