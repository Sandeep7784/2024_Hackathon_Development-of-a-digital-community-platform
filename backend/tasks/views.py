from django.shortcuts import render
from django.http import JsonResponse
from .Mongo import TaskManager
from users.models import Cookie
from django.views.decorators.csrf import csrf_exempt
import json

URI = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE = "Netropolis"
COLLECTION = "Tasks"
# Data Format: {'description': description, 'location': location}
@csrf_exempt
def addTask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        cookie = data.get('cookie', None)
        isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 2)
        if not isAuthorize:
            return JsonResponse({'message': 'Unauthorized'}, status=401)
        
        manager = TaskManager(URI, DATABASE, COLLECTION)
        taskId = manager.insert_task(data['description'], data['location'])
        return JsonResponse({'taskId': taskId}, status = 200)

# Data Format: {'taskId': taskId}
@csrf_exempt
def deleteTask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        cookie = data.get('cookie', None)
        isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 2)
        if not isAuthorize:
            return JsonResponse({'message': 'Unauthorized'}, status=401)

        manager = TaskManager(URI, DATABASE, COLLECTION)
        isDeleted = manager.delete_task(data['taskId'])
        return JsonResponse({'bool': isDeleted}, status = 200)
    
