from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from app01.views import mainmenu
from app01.models import goods_info
from django.http import JsonResponse

def state(request):
    pass

def good_details(request):
    pass

def good(request):
    good_id = request.GET.get('goodid')
    good = goods_info.objects.filter(id=good_id).first()
    return JsonResponse({'good_id': good.id, 'good_name': good.name, 'good_image': good.image, 'good_type': good.type, 'good_price': good.price, 'good_topic': good.topic, 'good_detail': good.detail, 'good_inventory': good.inventory, 'store_name': good.store.name})

def add_to_cart(request):
    good_id = request.POST.get('goodid')
    user_id = request.POST.get('user_id')
