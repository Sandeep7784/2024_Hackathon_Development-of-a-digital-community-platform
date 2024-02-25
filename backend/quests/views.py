from django.shortcuts import render
from django.http import JsonResponse
from Mongo import QuestManager
from ..users.models import Cookie
from ..users.community_manager_mongo import community_manager, client, db, collection
import json

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "Backend"
COLLECTION_NAME = "Quests"

# Data Format: {'tasks': [tasksId,....]}
def addQuest(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            
            tasks = data.get('tasks', [])
            if not tasks:
                return JsonResponse({'message': 'No tasks provided'}, status=400)

            manager = QuestManager(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
            questId = manager.insert_quest(tasks)

            communityManager = community_manager(client, db, collection)
            communityManager.insert_questId(isAuthorize.email, questId)
            
            return JsonResponse({'questId': questId}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

# Data Format: {'questId': questId}
def deleteQuest(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            questId = data.get('questId')
            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)

            if not questId:
                return JsonResponse({'message': 'No questId provided'}, status=400)

            manager = QuestManager(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
            isDeleted = manager.delete_quest(questId)
            return JsonResponse({'message': isDeleted}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
        
# Data Format: {'questId': questId, 'taskId': taskId}
def insertTask(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            questId = data.get('questId', None)
            taskId = data.get('taskId', None)

            if not questId or not taskId:
                return JsonResponse({'message': 'Both questId and taskId are required'}, status=400)

            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            
            manager = QuestManager(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
            isAdded = manager.add_task(questId=questId, taskId=taskId)
            return JsonResponse({'message': isAdded}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

# Data Format: {'questId': questId, 'taskId': taskId}
def deleteTask(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            questId = data.get('questId')
            taskId = data.get('taskId')

            if not questId or not taskId:
                return JsonResponse({'message': 'Both questId and taskId are required'}, status=400)

            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            
            manager = QuestManager(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
            isDeleted = manager.delete_task(questId=questId, taskId=taskId)
            return JsonResponse({'message': isDeleted}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)