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
    expiry = models.DateTimeField()

    @staticmethod
    def create(email):
        exists = Cookie.objects.filter(email = email).first()
        if exists:
            exists.delete()
        cookie = Cookie(email=email, cookie=str(uuid4()), expiry=datetime.now() + timedelta(days=30))
        cookie.save()
        return cookie.cookie
    
    @staticmethod
    def cookie_check(cookie, email):
        cookie_obj = Cookie.objects.filter(cookie=cookie).first()
        if not cookie_obj:
            return False
        if cookie_obj.email != email:
            return False
        if cookie_obj.expiry < datetime.now():
            return False
        return True