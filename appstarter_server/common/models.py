from django.db import models
from user.models import User

# Create your models here.
class Auth(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(max_length=128)
    accessToken = models.CharField(max_length=128)
    qqAccessToken = models.CharField(max_length=128)
    wechatAccessToken = models.CharField(max_length=128)
    weiboAccessToken = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Device(models.Model):
    deviceId = models.CharField(max_length=100)
    pushRegistrationId = models.CharField(max_length=100)
    currentUser = models.ForeignKey(User)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Coordinate(models.Model):
    user = models.ForeignKey(User)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    created = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    fileName = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    suffix = models.CharField(max_length=20)
    size = models.IntegerField
    uploadUser = models.ForeignKey(User)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Dictionary(models.Model):
    type = models.IntegerField
    value = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)