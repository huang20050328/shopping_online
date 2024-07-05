from django.db import models

class user_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    identity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', default='/static/img/default_image.png')
    sex = models.IntegerField(default=0)
    phonenum = models.IntegerField(null=True)

    class Meta:
        db_table = 'user_info'


class store_info(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_info, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phonenum = models.IntegerField()

    class Meta:
        db_table = 'store_info'

class goods_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='/static/img/good_default_image.png')
    type = models.IntegerField()
    price = models.IntegerField()
    topic = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    inventory = models.IntegerField()
    store = models.ForeignKey(store_info, on_delete=models.CASCADE)

    class Meta:
        db_table = 'goods_info'

class cart_info(models.Model):
    id = models.AutoField(primary_key=True)
    good = models.ForeignKey(goods_info, on_delete=models.CASCADE)
    user =models.ForeignKey("user_info",on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        db_table = 'cart_info'

class order_info(models.Model):
    id = models.AutoField(primary_key=True)
    good_id = models.IntegerField
    user_id = models.IntegerField
    user_address = models.CharField(max_length=100)
    user_phone = models.IntegerField()
    good_name = models.CharField(max_length=100)
    good_image = models.ImageField(upload_to='images/')
    good_price = models.IntegerField()
    count = models.IntegerField()
    state = models.IntegerField()
    price = models.IntegerField()
    way = models.IntegerField()
    reason = models.CharField(max_length=200)

    class Meta:
        db_table = 'order_info'

class address_info(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user_info, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    class Meta:
        db_table = 'address_info'