from django.shortcuts import render
from django.http import JsonResponse
from Mongo import TaskManager
import json

def addTask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uri = "mongodb://localhost:27017"
        database = "Backend"
        collection = "Tasks"
        manager = TaskManager(uri, database, collection)
        taskId = manager.insert_task(data['description'], data['location'])
        return JsonResponse({'taskId': taskId}, status = 200)

def deleteTask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uri = "mongodb://localhost:27017"
        database = "Backend"
        collection = "Tasks"
        manager = TaskManager(uri, database, collection)
        isDeleted = manager.delete_task(data['taskId'])
        return JsonResponse({'taskId': isDeleted}, status = 200)