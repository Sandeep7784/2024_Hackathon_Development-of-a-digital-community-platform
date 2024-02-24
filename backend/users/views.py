from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Cookie
import json

def login(request):
    if request.method == 'POST':
        try:
            # Extracting data from the body
            data = json.loads(request.body.decode('utf-8'))
            userEmail = data.get('email', None)
            userPassword = data.get('password', None)

            # Checking if email or password is None or not
            if not userEmail or not userPassword:
                return JsonResponse(status=204, data={'message': 'Email or Password is not given'})
            
            # Checking if user exits or not
            currUser = User.objects.filter(email = userEmail).first()
            if not currUser:
                return JsonResponse(data = {'message': 'User with the email does not exists'}, status=400)
            
            # Matching password
            if not check_password(userPassword, currUser.password):
                return JsonResponse(data = {'message': 'Email or password is wrong'}, status=401)
            
            newCookie = Cookie.create(userEmail)
            return JsonResponse(data = {'message': 'Login successful', 'user_type': currUser.user_type}, Cookie = newCookie)
        
        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
    pass