from django.shortcuts import render
from django.http import JsonResponse
from Mongo import TaskManager
from ..users.models import Cookie
import json

URI = "mongodb://localhost:27017"
DATABASE = "Backend"
COLLECTION = "Tasks"

# Data Format: {'description': description, 'location': location}
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