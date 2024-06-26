from django.db import models

class user_info(models.Model):
    id = models.AutoField(primary_key=True, default=10000003)
    name = models.CharField(max_length=100, default="用户"+str(id))
