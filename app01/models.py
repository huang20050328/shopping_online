from django.db import models

class user_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    balance = models.IntegerField(default=0)

