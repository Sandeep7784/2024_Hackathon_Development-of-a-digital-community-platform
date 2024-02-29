from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Cookie
import json
from .user_mongo import user
from .community_manager_mongo import community_manager
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
from quests.Mongo import QuestManager
from tasks.Mongo import TaskManager
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            # Extracting data from the body
            data = json.loads(request.body.decode('utf-8'))
            print(data)
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
            return JsonResponse(data = {'message': 'Login successful', 'user_type': currUser.user_type, 'cookie': newCookie})
        
        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body)
            userEmail = data.get('email' , '' ) 
            userPassword = make_password(data.get('password' , '' ))
            first_name = data.get('firstName' , '' ) 
            last_name = data.get('lastName' , '' ) 
            dob = data.get('dob' , '' ) 
            about = data.get('about' , '' )  
            
            if userEmail == None or userPassword == None or first_name == None or last_name == None or dob == None or about == None : 
                return JsonResponse(status=204, data={'message': 'Something is missing'})

           
            user_ = User.objects.filter(email=userEmail).first()
            
            if user_ : 
                return JsonResponse({'message': 'Email already exists'} , status = 401 )
            # client = "mongodb://localhost:27017/"
            client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            db =  'Netropolis'
            collection = 'user_data'
            
            manager = user(client=client , db=db , collection=collection) 
           
            manager.insert(email=userEmail , dob = dob , about= about)
            

            user_ = User(email = userEmail , password = userPassword , first_name = first_name , last_name = last_name ,user_type = 0 ) 
            user_.save()
            
            return JsonResponse(data = {'message' : 'Account Created Successfully.'} , status = 200 )
       
        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})

@csrf_exempt
def register_community_manager(request):
    if request.method == 'POST':
        try: 
            data = json.loads(request.body.decode('utf-8'))
            userEmail = data.get('email' , None ) 
            userPassword = make_password(data.get('password' , None ))
            first_name = data.get('first_name' , None ) 
            last_name = data.get('last_name' , None ) 
            dob = data.get('dob' , None ) 

            if userEmail == None or userPassword == None or first_name == None or last_name == None or dob == None  : 
                return JsonResponse(status=204, data={'message': 'Something is missing'})

            user1 = User.objects.filter(email=userEmail).first()
            
            if user1 : 
                return JsonResponse({'message': 'Email already exists'} , status = 401 )

            user1 = User(email = userEmail , password = userPassword , first_name = first_name , last_name = last_name ,user_type = 1 ) 
            user1.save()

            # client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            # db =  'Netropolis'
            # collection = 'user_data'
            # db_manager = community_manager(client=client , db=db , collection=collection) 
            
            # db_manager.insert(email=userEmail , dob = dob , about= about)

        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})

@csrf_exempt
def similarity(word1, word2):
    synsets1 = wordnet.synsets(word1)
    synsets2 = wordnet.synsets(word2)
    if synsets1 and synsets2:
        max_similarity = 0
        for synset1 in synsets1:
            for synset2 in synsets2:
                similarity = synset1.path_similarity(synset2)
                if similarity is not None and similarity > max_similarity:
                    max_similarity = similarity
        return max_similarity
    else:
        return 0  

@csrf_exempt
def search_query(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            query = data.get('query' , None ) 
            query_words = query.split(" ")
            # add changes 
            client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            db =  'Netropolis'
            collection = 'Quests'
            # yaha tak 
            quests = QuestManager(client , db , collection )
            quests_data = quests.get_all_quest_details()
            quests_priority = []
            for qId in quests_data:
                q_des = quests_data[qId]
                priorty = 0 
                for word1 in q_des:
                    for word2 in query_words:
                        priorty += similarity(word1 , word2 ) 
                # quests_priority[qId] = priorty 
                quests_priority.append([priorty , qId]) 
            quests_priority.sort() 
            quests_priority.reverse() 

            quests_priority = quests_priority[0:10]

            top_10_quests = {} 
            for q in quests_priority : 
                qid = q[1] 
                doc = quests.get_document(qid)
                tasks = doc['tasks']
                tilte = doc['title']
                top_10_quests[qid] = [tilte] + tasks

            return JsonResponse(top_10_quests , status = 200 )

        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})


@csrf_exempt 
def send_request(request) : 
    if(request.method == "POST") : 
        try:
            data = json.loads(request.body.decode('utf-8'))
            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            questId = data.get('questId' , None ) 
            client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            db =  'Netropolis'
            collection1 = 'Quests'
            
            quest_manager = QuestManager(client , db , collection1) 
            doc = quest_manager.get_document(questId)
            userEmail = cookie.email
            cm_email = doc['email']
            collection2 = 'community_manager_data'
            cm_object = community_manager(client , db , collection2)
            cm_object.get_request(cm_email , questId , userEmail , date_received = datetime.now()) 
            
            return JsonResponse({'message' : 'Request sent'}, status = 200 )


        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})

@csrf_exempt
def approve_request(request):
    if(request.method == "POST") : 
        try:
            data = json.loads(request.body.decode('utf-8'))
            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            questId = data.get('questId' , None ) 
            client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            db =  'Netropolis'
            collection1 = 'Quests'
            
            quest_manager = QuestManager(client , db , collection1) 
            doc = quest_manager.get_document(questId)
            userEmail = cookie.email
            cm_email = doc['email']
            collection2 = 'community_manager_data'
            cm_object = community_manager(client , db , collection2)
            cm_object.approve_quest(userEmail= userEmail , email = cm_email , questId= questId , status = 'approve') 
            
            return JsonResponse({'message' : 'Request approved'}, status = 200 )


        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})


@csrf_exempt
def reject_request(request):
    if(request.method == "POST") : 
        try:
            data = json.loads(request.body.decode('utf-8'))
            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            questId = data.get('questId' , None ) 
            client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            db =  'Netropolis'
            collection1 = 'Quests'
            
            quest_manager = QuestManager(client , db , collection1) 
            doc = quest_manager.get_document(questId)
            userEmail = cookie.email
            cm_email = doc['email']
            collection2 = 'community_manager_data'
            cm_object = community_manager(client , db , collection2)
            cm_object.approve_quest(userEmail= userEmail , email = cm_email , questId= questId , status = 'reject') 
            
            return JsonResponse({'message' : 'Request approved'}, status = 200 )


        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})


@csrf_exempt 
def get_all_tasks(request):
    if(request.method == "POST") : 
        try:
            data = json.loads(request.body.decode('utf-8'))
            cookie = data.get('cookie', None)
            isAuthorize = Cookie.cookie_check(cookie = cookie, userType = 1)
            if not isAuthorize:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
            
            client = "mongodb+srv://adarshshrivastava2003:qwerty0110@cluster0.bagywzw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            db =  'Netropolis'
            collection = 'Tasks'
            
            task_manager = TaskManager(client , db , collection) 
            all_tasks = task_manager.get_all_tasks() 
            return JsonResponse({'message' : 'Tasks Sent' , 'body' : all_tasks}, status = 200 )

        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})