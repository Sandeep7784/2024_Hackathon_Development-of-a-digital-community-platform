from pymongo import MongoClient

client = "mongodb://localhost:27017/"

db =  'Netropolis'

collection = 'community_manager_data'


class community_manager: 
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
                'approved_quests' : [] ,  # {['questId' , userEmail , start_date , end_date] }
                'pending_quests' : [] ,  # {['questId' , userEmail , date_recieved] }
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
    
    def delete_questId(self , email , questId)  :
        existing_user = self.collection.find_one({'email': email})
        if existing_user: 
            self.collection.update_one(
                {'email': email},
                {'$pull': {'quests': questId}}
            )
            print("QuestId deleted successfully.")
        else:
            print("Email Id does not exists ")

    def get_document(self , email ) : 
        isThere = self.collection.find_one(
            {"_id": email },
        )
        return isThere
    
    def approve_quest(self , email , questId , userEmail , start_date = "", end_date = "" , status = 'approve') : 
        existing_user = self.collection.find_one({'email': email})
        if existing_user:
            if questId in existing_user['quests']:
                approved_quest = {
                    'questId': questId,
                    'userEmail': userEmail,
                    'start_date': start_date,
                    'end_date': end_date
                }
                if status == 'approve':
                    self.collection.update_one(
                        {'email': email},
                        {'$push': {'approved_quests': approved_quest}}
                    )
                doc = existing_user
                print(doc['pending_quests'])
                date_recieved = None 
                pending_data = None 
                for i in doc['pending_quests']: 
                    print(i)
                    if(i['questId'] == questId):
                        pending_data = i 
                        date_recieved = i['date_recieved']
                # print(date_recieved)
                # date_received = doc['pending_quests']['date_received']
                # pending_data = {
                #     'questId' : questId , 
                #     'userEmail' : userEmail , 
                #     'date_received' : date_recieved , 
                # }
                print(pending_data)
                self.collection.update_one(
                    {'email' : email } , 
                    {'$pull' : {'pending_quests' : pending_data} }
                )
                print("Quest approved successfully")
            else:
                print("QuestId does not exist for the user")
        else:
            print("Email Id does not exist")

    def get_request(self , email , questId , userEmail , date_received = "") : 
        existing_user = self.collection.find_one({'email': email})
        if existing_user:
            new_data = {
                'questId': questId,
                'userEmail': userEmail,
                'date_recieved': date_received,
            }
            self.collection.update_one(
                {'email' : email } , 
                {'$push' : {'pending_quests' : new_data} }
            )
            print("Request recieved ")
        else : 
            print("Email Id does not exist")

# xy = community_manager(client=client , db =db , collection=collection) 
# xy.insert('cm1@netropolis.ac.in' , dob = 'dob') 
# xy.insert('cm2@netropolis.ac.in' , dob = 'dob') 
# xy.insert('cm3@netropolis.ac.in' , dob = 'dob') 
# xy.insert_questId(email='cm1@netropolis.ac.in' , questId= 23 ) 
# xy.get_request("cm1@netropolis.ac.in" , 23 , 'user1' , 'date1')
# xy.approve_quest("cm1@netropolis.ac.in" , 23 , "user1"  )
# xy.approve_quest(email='cm1@netropolis.ac.in' , questId=23 , userEmail='abc1@gmail.com' ,  start_date='start_date' , end_date= 'end_date')