from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Cookie
import json
from user_mongo import user
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
from backend.quests.Mongo import QuestManager

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
        try:
            data = json.loads(request.body.decode('utf-8'))
            userEmail = data.get('email' , None ) 
            userPassword = make_password(data.get('password' , None ))
            first_name = data.get('first_name' , None ) 
            last_name = data.get('last_name' , None ) 
            dob = data.get('dob' , None ) 
            about = data.get('about' , None )  

            if userEmail == None or userPassword == None or first_name == None or last_name == None or dob == None or about == None : 
                return JsonResponse(status=204, data={'message': 'Something is missing'})

            user_ = User.objects.filter(email=userEmail).first()
            
            if user_ : 
                return JsonResponse({'message': 'Email already exists'} , status = 401 )
            client = "mongodb://localhost:27017/"
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

            user = User.objects.filter(email=userEmail).first()
            
            if user : 
                return JsonResponse({'message': 'Email already exists'} , status = 401 )

            user = User(email = userEmail , password = userPassword , first_name = first_name , last_name = last_name ,user_type = 1 ) 
            user.save()

        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})

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


def search_query(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8')) 
            query = data.get('query' , None ) 
            query_words = query.split(" ")
            # add changes 
            client = 'add_client'
            db ='db'
            collection = 'collection'
            # yaha tak 
            quests = QuestManager(client , db , collection )
            quests_data = quests.get_all_quest_details()
            quests_priority = {}
            for qId in quests_data:
                q_des = quests_data[qId]
                priorty = 0 
                for word1 in q_des:
                    for word2 in query_words:
                        priorty += similarity(word1 , word2 ) 
                quests[qId] = priorty
                
            return quests 

        except Exception as e:
            print(f"An error occured: {e}")
            JsonResponse({'message': e})