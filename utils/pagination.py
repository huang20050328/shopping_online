import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict

from app01.models import CartInfo
from app01.models import GoodsInfo, OrderInfo
from shopping import settings


def paginate(page, good_type, user_id, where):
    page = page
    good_type = good_type
    user_id = user_id
    where = where
    good_lst = []
    if where == 0:  # 商城主页
        good_lst = GoodsInfo.objects.all()
    if where == 1:  # 分类页
        good_lst = GoodsInfo.objects.filter(type=good_type).all()
    if where == 2:  # 购物车页
        good_lst = CartInfo.objects.filter(user_id=user_id).all()

        paginator = Paginator(good_lst, 20)

        try:
            current_page = paginator.page(page)
        except PageNotAnInteger:
            current_page = paginator.page(1)
        except EmptyPage:
            current_page = paginator.page(1)

        good_lst = [dict(model_to_dict(i), **{'image': os.path.join(settings.MEDIA_URL, 'img/', i.good.image)}) for i in
                    good_lst]

        response_data = {
            'goods': good_lst,
            'current_page': current_page.number,
            'total_pages': paginator.num_pages,
            'has_next': current_page.has_next(),
            'has_previous': current_page.has_previous()
        }

        return response_data

    if where == 3:  # 订单页
        good_lst = OrderInfo.objects.filter(user_id=user_id).all()

    paginator = Paginator(good_lst, 20)

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(1)

    good_lst = [dict(model_to_dict(i)) for i in
                good_lst]

    response_data = {
        'goods': good_lst,
        'current_page': current_page.number,
        'total_pages': paginator.num_pages,
        'has_next': current_page.has_next(),
        'has_previous': current_page.has_previous()
    }

    return response_data
