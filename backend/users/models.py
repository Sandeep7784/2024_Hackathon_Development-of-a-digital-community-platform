from django.db import models
from datetime import datetime, timedelta
from uuid import uuid4

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=500)
    user_type = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Cookie(models.Model):
    email = models.CharField(max_length=50)
    cookie = models.CharField(max_length=40)

    @staticmethod
    def create(email):
        exists = Cookie.objects.filter(email = email).first()
        if exists:
            exists.delete()
        cookie = Cookie(email=email, cookie=str(uuid4()))
        cookie.save()
        return cookie.cookie
    
    @staticmethod
    def cookie_check(cookie, userType):
        cookie_obj = Cookie.objects.filter(cookie=cookie).first()
        if not cookie_obj:
            return False
        user = User.objects.filter(email = cookie_obj.email)
        if user.user_type != userType:
            return False
        return cookie_obj