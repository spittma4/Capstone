#stuar
from database import Database
import pymysql
import unittest
DB_PATH = "localhost"

def create_database():
    connection = pymysql.connect(host=DB_PATH, user="root", database="test")
    cur = connection.cursor()
    cur.execute("CREATE TABLE users (email varchar(25),salt varchar(15), hash varchar(64), twitter varchar(15))")
    return cur

def tear_down_database(cur):
    cur.execute("DROP TABLE users")


    

if __name__ == "__main__" :
   cur=create_database()
   Database.insert_user("jim@school.com", "doggie", "Jim James")
   tear_down_database(cur)
