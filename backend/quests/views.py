from django.shortcuts import render
from django.http import JsonResponse
from Mongo import QuestManager
import json

# Data Format: {'tasks': [tasksId,....]}
def addQuest(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uri = "mongodb://localhost:27017"
        database = "Backend"
        collection = "Quests"
        manager = QuestManager(uri, database, collection)
        questId = manager.insert_quest(data['tasks'])
        return JsonResponse({'questId': questId}, status = 200)

# Data Format: {'questId': questId}
def deleteQuest(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uri = "mongodb://localhost:27017"
        database = "Backend"
        collection = "Quests"
        manager = QuestManager(uri, database, collection)
        isDeleted = manager.delete_quest(data['questId'])
        return JsonResponse({'bool': isDeleted}, status = 200)

# Data Format: {'questId': questId, 'taskId': taskId}
def insertTask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uri = "mongodb://localhost:27017"
        database = "Backend"
        collection = "Quests"
        manager = QuestManager(uri, database, collection)
        isAdded = manager.add_task(questId = data['questId'], taskId = data['taskId'])
        return JsonResponse({'bool': isAdded}, status = 200)
    
# Data Format: {'questId': questId, 'taskId': taskId}
def deleteTask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uri = "mongodb://localhost:27017"
        database = "Backend"
        collection = "Quests"
        manager = QuestManager(uri, database, collection)
        isDeleted = manager.delete_task(questId = data['questId'], taskId = data['taskId'])
        return JsonResponse({'bool': isDeleted}, status = 200)