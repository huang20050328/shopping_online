# Generated by Django 5.0.6 on 2024-07-09 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('good_id', models.IntegerField(null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('user_address', models.CharField(max_length=100)),
                ('user_phone', models.IntegerField()),
                ('good_name', models.CharField(max_length=100)),
                ('good_image', models.ImageField(upload_to='images/')),
                ('good_price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('state', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('way', models.IntegerField()),
                ('reason', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'order_info',
            },
        ),
        migrations.CreateModel(
            name='StoreInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phonenum', models.IntegerField()),
            ],
            options={
                'db_table': 'store_info',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('balance', models.IntegerField(default=0)),
                ('identity', models.IntegerField(default=0)),
                ('image', models.TextField(default='default.jpg')),
                ('sex', models.IntegerField(default=0)),
                ('phonenum', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField(default='default.jpg')),
                ('type', models.IntegerField()),
                ('price', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=200)),
                ('inventory', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.storeinfo')),
            ],
            options={
                'db_table': 'goods_info',
            },
        ),
        migrations.AddField(
            model_name='storeinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.userinfo'),
        ),
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.goodsinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.userinfo')),
            ],
            options={
                'db_table': 'cart_info',
            },
        ),
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.userinfo')),
            ],
            options={
                'db_table': 'address_info',
            },
        ),
    ]
