from pymongo import MongoClient

client = "mongodb://localhost:27017/"

db =  'Netropolis'

collection = 'community_manager_data'


class community_manager : 
    def __init__(self , client , db , collection) : 
        self.client = MongoClient(client)
        self.db = self.client[db]
        self.collection = self.db[collection] 

    def insert(self , email , dob  ) : 
        existing_user = self.collection.find_one({'email': email})
        if(existing_user):
            print("Email Id already exists") 
        else:
            user_doc = {
                'email': email,
                'dob' : dob ,
                'quests' : [] , # {'questId' : (idofquest)  }
                'approved_quests' : [] # {['questId' , userEmail , start_date , end_date] }
                
            }
            self.collection.insert_one(user_doc)
    
    def insert_questId(self , email , questId)  :
        existing_user = self.collection.find_one({'email': email})
        if existing_user: 
            self.collection.update_one(
                {'email': email},
                {'$push': {'quests': questId}}
            )
        else:
            print("Email Id does not exists ")
    
    def approve_quest(self , email , questId , userEmail , start_date , end_date ) : 
        existing_user = self.collection.find_one({'email': email})
        if existing_user:
            if questId in existing_user['quests']:
                approved_quest = {
                    'questId': questId,
                    'userEmail': userEmail,
                    'start_date': start_date,
                    'end_date': end_date
                }
                self.collection.update_one(
                    {'email': email},
                    {'$push': {'approved_quests': approved_quest}}
                )
                print("Quest approved successfully")
            else:
                print("QuestId does not exist for the user")
        else:
            print("Email Id does not exist")

# xy = community_manager(client=client , db =db , collection=collection) 
# xy.insert('cm1@netropolis.ac.in' , dob = 'dob') 
# xy.insert('cm2@netropolis.ac.in' , dob = 'dob') 
# xy.insert('cm3@netropolis.ac.in' , dob = 'dob') 
# xy.insert_questId(email='cm1@netropolis.ac.in' , questId= 23 ) 
# xy.approve_quest(email='cm1@netropolis.ac.in' , questId=23 , userEmail='abc1@gmail.com' ,  start_date='start_date' , end_date= 'end_date')