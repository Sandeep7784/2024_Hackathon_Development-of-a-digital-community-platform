from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import json

def login(request):
    if request.method == 'POST':
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
            # Status is missing
            return JsonResponse(data = {'message': 'User with the email does not exits'})
        
        # Matching password
        if not check_password(userPassword, currUser.password):
            return JsonResponse(data = {'message': 'Email or password is wrong'}, status=401)
        