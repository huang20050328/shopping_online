from django.forms import model_to_dict
from django.shortcuts import render
from app01.models import GoodsInfo

from django.http import JsonResponse
import os
from django.conf import settings
from utils import app_jwt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@app_jwt.decorator_login_require
def state(request):
    return JsonResponse({'code': 0, 'user_id': request.user.id})


# """
#     首页验证用户登录状态，并获取用户id
#     """
#     try:
#         token = request.META.get("HTTP_AUTHORIZATION")
#         decoded_payload = jwt.decode(token, 'jian_guo_lang_lang', algorithms=['HS256'])
#         user = user_info.objects.filter(username=decoded_payload['user_name']).first()
#         return JsonResponse({'code': 0, 'user_id': user.id})
#     except jwt.ExpiredSignatureError:
#         return JsonResponse({'code': 1})
#     except jwt.InvalidTokenError:
#         return JsonResponse({'code': 1})


def main_menu(request):
    return render(request, 'main_menu.html')


def good_list(request):
    """
    首页商品列表接口
    """
    page = request.GET.get('page', 1)
    query = GoodsInfo.objects.all()
    paginator = Paginator(query, 20)

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(1)

    good_lst = [dict(model_to_dict(i), **{'image': os.path.join(settings.MEDIA_URL, 'img', i.image)}) for i in
                query]

    response_data = {
        'goods': good_lst,
        'current_page': current_page.number,
        'total_pages': paginator.num_pages,
        'has_next': current_page.has_next(),
        'has_previous': current_page.has_previous()
    }

    return JsonResponse(response_data, safe=False)
