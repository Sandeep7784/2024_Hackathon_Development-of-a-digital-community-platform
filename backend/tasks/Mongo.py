from pymongo import MongoClient

class TaskManager:
    def __init__(self, mongo_uri, database_name, collection_name):
        self.connection = MongoClient(mongo_uri)
        self.database = self.connection[database_name]
        self.collection = self.database[collection_name]

    def insert_task(self, description, location):
        task_id = self.get_next_task_id()
        task_document = {"_id": task_id, "description": description, "location": location}
        self.collection.insert_one(task_document)
        return task_id

    def delete_task(self, task_id):
        result = self.collection.delete_one({"_id": task_id})
        return result.deleted_count > 0

    def get_next_task_id(self):
        counter_collection = self.database["TaskCounter"]
        counter_doc = counter_collection.find_one_and_update(
            {"_id": "task_id"},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=True,
        )
        return counter_doc["seq"]

    def get_description(self, taskId):
        res = self.collection.find({"_id": taskId})
        compelete_description = res.description + 'Location : ' + res.location
        output = {'description': compelete_description}
        return output
    
    def get_document(self , taskId ) : 
        isThere = self.collection.find_one(
            {"_id": taskId},
        )
        return isThere

    def get_all_tasks(self): 
        result = self.collection.find({})
        return result