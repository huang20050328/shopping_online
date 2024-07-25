import os

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from app01.models import CartInfo
from shopping import settings
from utils import app_jwt, pagination
from django.http import QueryDict


@app_jwt.decorator_login_require
def state(request):
    return JsonResponse({'code': 0, 'user_id': request.user.id})


def cart(request):
    return render(request, 'cart_page.html')


def cart_list(request):
    user_id = request.POST.get('user_id')
    page = request.POST.get('page', 1)
    response_data = pagination.paginate(page, None, user_id, 2)
    # response_data = CartInfo.objects.filter(user_id=user_id).all()
    # response_data = [dict(model_to_dict(i)) for i in response_data]
    return JsonResponse(response_data, safe=False)


def cart_remove(request):
    # cart_id = request.DELETE.get('cart_id')
    params = QueryDict(request.body)
    print(params)

    # 此时params 就是一个python字典
    cart_id = params.get("cart_id")
    print(cart_id)
    CartInfo.objects.filter(id=cart_id).delete()
    return HttpResponse("移除成功")


def cart_update(request):
    pass
