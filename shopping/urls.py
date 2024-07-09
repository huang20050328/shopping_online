"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', (include('blog.urls'))
"""
from django.contrib import admin
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
from django.urls import path
from app01.views import add_user_image

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', mainmenu.main_menu),  # 商城首页
                  path('state/', mainmenu.state),  # 首页登录状态接口
                  path('good_list/', mainmenu.good_list),  # 首页商品列表接口
                  path('registration/', login.registration),  # 注册页面
                  path('registration/verifying/', login.registration_verifying),  # 注册判断接口
                  path('login/', login.login),  # 登录页面
                  path('login/verifying/', login.verifying),  # 登录判断接口
                  path('changepwd/', login.change_pwd),  # 修改密码页面
                  path('changepwd/verifying/', login.change_pwd_verifying),  # 修改密码判断接口
                  path('category/', category_page.category_page),  # 分类页面
                  path('category/good_list/', category_page.good_list),  # 分类页商品列表接口
                  path('details/', good_details.good_details),  # 商品详情页
                  path('details/good/', good_details.good),  # 商品详情页商品信息接口
                  path('details/addtocart/', good_details.add_to_cart),  # 商品详情页添加购物车接口
                  path('cart/', cart.cart),  # 购物车页
                  path('cart/cart_list/', cart.cart_list),  # 购物车列表接口
                  path('cart/cart_remove/', cart.cart_remove),  # 移除购物车接口
                  path('cart/cart_update/', cart.cart_update),  # 购物车更新接口
                  path('order/', order.order),  # 订单页
                  path('order/order_list/', order.order_list),  # 订单列表接口
                  path('order/refund_apply/', order.refund_apply),  # 订单售后接口
                  path('pay/', pay_page.pay_page),  # 支付页面
                  path('pay/cart/', pay_page.from_cart),  # 购物车结算的商品信息接口
                  path('pay/details/', pay_page.from_details),  # 商品详情页面直接购买的商品信息接口
                  path('pay/order/', pay_page.from_order),  # 订单页再来一单的商品信息接口
                  path('pay/submit/', pay_page.submit),  # 订单结算接口
                  path('user/', user_page.user_page),  # 个人信息页
                  path('user/info/', user_page.user_info),  # 个人信息列表接口
                  path('user/update/', user_page.info_update),  # 信息更新接口
                  path('user/delete/', user_page.delete_user),  # 账号注销接口
                  path('add_user_image/', add_user_image.add_user_image, name='add_user_image'),
                  path('upload_handle/', add_user_image.upload_handle, name='upload_handle'),
                  path('show_avatar/', add_user_image.show_avatar, name='show_avatar'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
