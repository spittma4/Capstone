from pymongo import MongoClient
from bson.objectid import ObjectId

def set_client(address):
    return MongoClient(address)

def set_db(client,DBname):
    return client[DBname]

def set_collection(DB,collection):
    return DB.[collection]

def read_collection(collection):
    fromMongo = list(collection.find())
    return result

def write_collection(collection,listDict):
    
