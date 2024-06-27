"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to v. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function v
    1. Add an import:  from my_app import v
    2. Add a URL to urlpatterns:  path('', v.home, name='home')
Class-based v
    1. Add an import:  from other_app.v import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.v import login


def index(request):
    models.user_info.objects.all().delete()
    if models.user_info.objects.filter(id=10000000).exists():
        models.user_info.objects.create()
        id=models.user_info.objects.last().id
        models.user_info.objects.filter(id=id).update(name="用户"+str(id))
    else:
        models.user_info.objects.create(id=10000000)
        id = models.user_info.objects.last().id
        models.user_info.objects.filter(id=id).update(name="用户"+str(id))
    return HttpResponse("添加成功")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', login.registration),
    path('login/', login.login),
    path('login/verifying', login.verifying)
]
