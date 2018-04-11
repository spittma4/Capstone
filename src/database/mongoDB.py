from pymongo import MongoClient
from bson.objectid import ObjectId

class Mongo:
    def __init__(self):
        

    def set_client(self, address):
        self.client = MongoClient(address)
        
    def set_db(self, client, DBname):
        self.db = client[DBname]
            
    def set_collection(self, collection):
        self.collection = self.db.[collection]

    def read_collection(self):
        fromMongo = list(self.collection.find())
        return result

    def write_tweets(self, tweets):
        #store text, retweets and favorites
        #takes list of tuples
        for tweet in tweets:
            self.collection.insert({
                "_text":tweet[0],
                "_favCount":tweet[1]
                "_retweetCount":tweet[2],
            })


