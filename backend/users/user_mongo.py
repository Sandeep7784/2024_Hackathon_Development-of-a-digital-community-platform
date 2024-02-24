from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")

# db =  'Netropolis'

# collection = 'user_data'


class user : 
    def __init__(self , client , db , collection) : 
        self.client = MongoClient(client)
        self.db = self.client[db]
        self.collection = self.db[collection] 

    def insert(self , email , dob , about ) : 
        existing_user = self.collection.find_one({'email': email})
        if(existing_user):
            print("Email Id already exists") 
        else:
            user_doc = {
                'email': email,
                'dob' : dob ,
                'About' : about , 
                'quests' : [] , # {'questId' : (idofquest) , 'start_date': () , 'end_date' : (), 'schedule' : () }
                'pending_requests' : [] ,  # {'questId' : (id_of_quest) , 'request_timestamp' : (datetime) }
                'rejected_requests' : [] ,  # {'questId' : (id_of_quest) , 'request_timestamp' : (datetime) }
                # 'feedbacks' : {} , # {'mesages' , 'timestamp' }  
                'search_history' : [] # { 'query' : (string) , 'timestamp' : datetime }
            }
            self.collection.insert_one(user_doc)
    

    def request_quest(self , email , questId , timestamp  ) : 
        existing_user = self.collection.find_one({'email' : email }) 
        if existing_user : 
            request_doc = {
                'questId': questId,
                'timestamp': timestamp,
            }

            self.collection.update_one( 
                {'email': email},
                {'$push': {'pending_requests': request_doc}}
            )

    def withdraw_request(self, email, questId):
        existing_user = self.collection.find_one({'email': email})
        if existing_user:
            self.collection.update_one(
                {'email': email},
                {'$pull': {'pending_requests': {'questId': questId}}}
            )
            print("Request withdrawn successfully")
        else:
            print("User not found")
    
    def update_status(self, email, questId, approved , schedule = None , start_date = None , end_date = None ):
        existing_user = self.collection.find_one({'email': email})
        if existing_user:
            query = {'email': email}
            update_query = {}
            if approved:
                update_query = {
                    '$pull': {'pending_requests': {'questId': questId}},
                    '$push': {'quests': {'questId': questId, 'schedule': schedule, 'start_date': start_date, 'end_date': end_date}}
                }
            else:
                update_query = {
                    '$pull': {'pending_requests': {'questId': questId}},
                    '$push': {'rejected_requests': {'questId': questId}}
                }
            self.collection.update_one(query, update_query)
            print("Status updated successfully")
        else:
            print("User not found")


# xy = user(client=client , db = db , collection = collection) 
# xy.insert("abc1@gmail.com")
# xy.insert("abc2@gmail.com")
# xy.insert("abc3@gmail.com")

# xy.request_quest(email= "abc1@gmail.com" , questId= 13 , timestamp='Any') 
# xy.request_quest(email= "abc2@gmail.com" , questId= 23 , timestamp='Any') 
# xy.request_quest(email= "abc3@gmail.com" , questId= 33 , timestamp='Any') 
# xy.withdraw_request("abc@gmail.com" , 83 ) 
# xy.update_status( 'abc1@gmail.com' , questId=83 , approved=True)