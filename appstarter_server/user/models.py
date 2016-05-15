from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    userType = models.IntegerField()
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    realName = models.CharField(max_length=20)
    nickName = models.CharField(max_length=20)
    registerTime = models.DateField
    city = models.CharField(max_length=20)
    qq = models.CharField(max_length=20)
    wechat = models.CharField(max_length=20)
    hobby = models.CharField(max_length=100)
    introduction = models.CharField(max_length=500)
    birthday = models.DateField
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

