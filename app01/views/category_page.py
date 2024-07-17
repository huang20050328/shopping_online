from django.http import JsonResponse
from django.shortcuts import render

from utils import pagination


def category_page(request):
    return render(request, 'category_page.html')


def good_list(request):
    good_type = request.GET.get('type')
    page = request.GET.get('page', 1)
    response_data = pagination.paginate(page, good_type, None, 1)

    return JsonResponse(response_data, safe=False)
