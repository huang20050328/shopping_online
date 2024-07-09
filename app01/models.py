from django.db import models


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    identity = models.IntegerField(default=0)
    image = models.TextField(default="default.jpg")
    sex = models.IntegerField(default=0)
    phonenum = models.IntegerField(null=True)

    class Meta:
        db_table = 'user_info'


class StoreInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phonenum = models.IntegerField()

    class Meta:
        db_table = 'store_info'


class GoodsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.TextField(default="default.jpg")
    type = models.IntegerField()
    price = models.IntegerField()
    topic = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    inventory = models.IntegerField()
    store = models.ForeignKey(StoreInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'goods_info'


class CartInfo(models.Model):
    id = models.AutoField(primary_key=True)
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    user = models.ForeignKey("UserInfo", on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        db_table = 'cart_info'


class OrderInfo(models.Model):
    id = models.AutoField(primary_key=True)
    good_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=100, null=True)
    user_address = models.CharField(max_length=100)
    user_phone = models.IntegerField(null=True)
    good_name = models.CharField(max_length=100)
    good_image = models.TextField(max_length=200, null=True)
    good_price = models.IntegerField()
    count = models.IntegerField()
    state = models.IntegerField(default=0)  # 0为已完成 1为订单取消 2为售后申请中
    price = models.IntegerField(null=True)
    way = models.IntegerField(null=True)
    reason = models.CharField(max_length=200, null=True)
    time_buy = models.DateTimeField(auto_now_add=True, null=True)
    time_apply = models.DateTimeField(null=True)
    time_refund = models.DateTimeField(null=True)

    class Meta:
        db_table = 'order_info'


class AddressInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'address_info'
