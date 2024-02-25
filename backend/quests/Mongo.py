from pymongo import MongoClient
from ..tasks.Mongo import TaskManager
from ..tasks.views import URI, DATABASE, COLLECTION

class QuestManager:
    def __init__(self, mongo_uri, database_name, collection_name):
        self.connection = MongoClient(mongo_uri)
        self.database = self.connection[database_name]
        self.collection = self.database[collection_name]

    def insert_quest(self, tasks , title ):
        quest_id = self.get_next_quest_id()
        quest_document = {"_id": quest_id, "tasks": tasks , "title" : title}
        self.collection.insert_one(quest_document)
        return quest_id

    def delete_quest(self, quest_id):
        result = self.collection.delete_one({"_id": quest_id})
        return result.deleted_count > 0
    
    def add_task(self, questId, taskId):
        isThere = self.collection.find_one_and_update(
            {"_id": questId},
            {"$addToSet": {"tasks": taskId}}
        )
        return isThere.modified_count > 0

    def delete_task(self, quest_id, task_id):
        result = self.collection.update_one(
            {"_id": quest_id},
            {"$pull": {"tasks": task_id}}
        )
        return result.modified_count > 0
    
    def get_next_quest_id(self):
        counter_collection = self.database["QuestCounter"]
        counter_doc = counter_collection.find_one_and_update(
            {"_id": "quest_id"},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=True,
        )
        return counter_doc["seq"]
    
    def get_all_quest_details(self):
        quest_details = {}
        quests = self.collection.find({})
        for quest in quests:
            descriptions = []
            for taskId in quest.tasks:
                descriptions.append(self.task_description(taskId))
            quest_details[quest._id] = descriptions
        return quest_details

    def task_description(self, taskId):
        manager = TaskManager(URI, DATABASE, COLLECTION)
        return manager.get_description(taskId)