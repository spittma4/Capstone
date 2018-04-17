from pymongo import MongoClient
from bson.objectid import ObjectId
from . import private as p

class Mongo:
    def __init__(self, email, tweet=None):
        address="mongodb://{}:{}@ds019866.mlab.com:19866/ksusocialsuite".format(p.mongo_username, p.mongo_password)
        self.client = MongoClient(address) 
        self.db = self.client['ksusocialsuite']
        self.email = email.replace('@', '---')
        
        if self.collection_exists() == False:
            self.collection = self.db.create_collection(self.get_email())
        else:
            self.collection = self.db[self.get_email()]
        
        if tweet:
            self.write_tweet(tweet)
        
    def get_email(self):
        x = self.email
        return x

    def read_collection(self):
        fromMongo = list(self.collection.find())
        entries = []
        for entry in fromMongo:
            entries.append( entry['_text'])
        return entries

    def write_tweet(self, tweet):
        #store text, retweets and favorites
        #takes list of tuples
        self.collection.insert_one({
            "_text":tweet
        })
    
    def collection_exists(self):
        collections = self.db.collection_names()
        for collection in collections:
            if collection == self.email:
                return True
        return False
