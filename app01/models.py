from django.db import models

class user_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)

