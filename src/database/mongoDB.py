from pymongo import MongoClient
from bson.objectid import ObjectId
import private as p

class Mongo:
    def __init__(self, email, tweet=None):
        address="mongodb://{}:{}@ds019866.mlab.com:19866/ksusocialsuite".format(p.mongo_username, p.mongo_password)
        self.client = MongoClient(address) 
        self.db = client['ksusocialsuite']
        self.email = email.replace('@', '...')
        self.collection = self.db[self.email]
        if tweet:
            self.write_tweet(tweet)

    def read_collection(self):
        fromMongo = list(self.collection.find())
        return result

    def write_tweets(self, tweet):
        #store text, retweets and favorites
        #takes list of tuples
        self.collection.insert_one({
            "_text":tweet
        })


