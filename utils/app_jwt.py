from django.http import JsonResponse
from app01.models import user_info
import jwt
from rest_framework_jwt.settings import api_settings


def jwt_get_secret_key(payload=None):
    return api_settings.JWT_SECRET_KEY


def jwt_encode_handler(payload):
    key = api_settings.JWT_PRIVATE_KEY or jwt_get_secret_key(payload)
    return jwt.encode(
        payload,
        key,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')


def jwt_decode_handler(token):
    options = {
        'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
    }
    # get user from token, BEFORE verification, to get user secret key
    unverified_payload = jwt.decode(token, None, False)
    secret_key = jwt_get_secret_key(unverified_payload)
    return jwt.decode(
        token,
        api_settings.JWT_PUBLIC_KEY or secret_key,
        api_settings.JWT_VERIFY,
        options=options,
        leeway=api_settings.JWT_LEEWAY,
        audience=api_settings.JWT_AUDIENCE,
        issuer=api_settings.JWT_ISSUER,
        algorithms=[api_settings.JWT_ALGORITHM]
    )


def decorator_login_require(func):
    """登录装饰器"""

    def wrapper(request, *args, **kwargs):
        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        print(authorization)# 获取Headers里的Authorization值
        if authorization:
            payload = jwt_decode_handler(authorization)
            user_id = payload['user_id']
            user = user_info.objects.filter(id=user_id).first()  # 解密后查询
            if user:
                request.user = user
                return func(request, *args, **kwargs)
        return JsonResponse({"code": 401, "msg": "未登录"})

    return wrapper
