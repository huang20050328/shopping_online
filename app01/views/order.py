import os
from django.utils import timezone

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from app01.models import OrderInfo
from shopping import settings


def order(request):
    """
    返回订单页面
    """
    return render(request, 'order.html')


def order_list(request):
    """
    订单列表接口
    """
    user_id = request.POST.get('user_id')
    user_order = OrderInfo.objects.filter(user_id=user_id).all()
    order_lst = [dict(model_to_dict(i), **{'image': os.path.join(settings.MEDIA_URL, 'img', i.good_image)}) for i in
                 user_order]
    return JsonResponse(order_lst, safe=False)


def refund_apply(request):
    """
    售后申请接口
    """
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        way = request.POST.get('way')
        reason = request.POST.get('reason')
        OrderInfo.objects.filter(id=order_id).update(way=way, reason=reason, state=1, time_cancel=timezone.now())
        return HttpResponse('售后申请成功')
    return JsonResponse({'code': 1})
