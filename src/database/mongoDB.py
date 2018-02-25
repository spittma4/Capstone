from pymongo import MongoClient
from bson.objectid import ObjectId

def set_client(address):
    return MongoClient(address)

def set_db(client,DBname):
    return client[DBname]

def set_collection(DB,collection):
    return DB.[collection]

def read_collection(collection):
    pre = list(collection.find())
    for item in pre:
        del item['_id']
    result = []
    for entry in pre:
        info = (
            entry['_tweet']
            time['_time']
        )
        result.append(tuple(info))
    return result
