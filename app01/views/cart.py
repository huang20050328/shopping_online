import os

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from app01.models import CartInfo
from shopping import settings
from utils import app_jwt, pagination


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
    pass


def cart_update(request):
    pass
