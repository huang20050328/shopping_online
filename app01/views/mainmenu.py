from django.http import JsonResponse
from django.shortcuts import render

from utils import app_jwt
from utils import pagination


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
    response_data = pagination.paginate(page, None)

    return JsonResponse(response_data, safe=False)
