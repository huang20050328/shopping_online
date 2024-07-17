import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict

from app01.models import GoodsInfo
from shopping import settings


def paginate(page, good_type):
    good_type = good_type
    page = page
    if good_type:
        good_lst = GoodsInfo.objects.filter(type=good_type).all()
    else:
        good_lst = GoodsInfo.objects.all()
    paginator = Paginator(good_lst, 20)
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(1)

    good_lst = [dict(model_to_dict(i), **{'image': os.path.join(settings.MEDIA_URL, 'img/', i.image)}) for i in
                good_lst]

    response_data = {
        'goods': good_lst,
        'current_page': current_page.number,
        'total_pages': paginator.num_pages,
        'has_next': current_page.has_next(),
        'has_previous': current_page.has_previous()
    }

    return response_data
