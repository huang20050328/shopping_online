"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.views import login
from app01.views import mainmenu
from app01.views import good_details
from app01.views import cart
from app01.views import category_page
from app01.views import pay_page
from app01.views import order
from app01.views import user_page
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from app01.views import add_user_image



def index(request):
    models.user_info.objects.all().delete()
    #models.user_info.objects.create(id=10000000)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', login.registration),
    path('registration/verifying/', login.registration_verifying),
    path('login/', login.login),
    path('login/verifying/', login.verifying),
    path('changepwd/', login.change_pwd),
    path('changepwd/verifying/', login.change_pwd_verifying),
    path('', mainmenu.mainmenu),
    path('state/', mainmenu.state),
    path('good_list/', mainmenu.good_list),
    path('categorypage/', category_page.category_page),
    path('categorypage/good_list/', category_page.good_list),
    path('details/', good_details.good_details),
    path('details/good/', good_details.good),
    path('details/addtocart/', good_details.add_to_cart),
    path('cart/', cart.cart),
    path('cart/cart_list/', cart.cart_list),
    path('cart/cart_remove/', cart.cart_remove),
    path('cart/cart_update/', cart.cart_update),
    path('order/', order.order),
    path('order/order_list/', order.order_list),
    path('pay/', pay_page.pay_page),
    path('pay/cart/', pay_page.from_cart),
    path('pay/details/', pay_page.from_details),
    path('pay/order/', pay_page.from_order),
    path('pay/submit/', pay_page.submit),
    path('user/', user_page.user_page),
    path('user/info/', user_page.user_info),
    path('user/update/', user_page.info_update),
    path('user/delete/', user_page.delete_user),
    path('add_user_image/', add_user_image.add_user_image, name='add_user_image'),
    path('upload_handle/', add_user_image.upload_handle, name='upload_handle'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
