# Generated by Django 5.0.6 on 2024-06-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_user_info_balance_user_info_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
