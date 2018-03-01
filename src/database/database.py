#Jack
#Stuart

import string
import pymysql
import hashlib
import random

DB_PATH = "localhost"
DATABASE_ERROR = 1
class Database:
    connection=None
    def __init__(self):
        self.connection = pymysql.connect(host=DB_PATH, user="root", database="prod")

    def generate_salt():
        salt = ""
        for i in range(0,15):
            salt+=random.choice(string.letters)
        return salt
        
    def sanitize(self, inString):
        result = 
    
    def check_login(self, email, password, db=self.connection):
        pass

    def user_exists(self, email, db=self.connection):
        cur = db.cursor()
        try:
           result = cur.fetchall("select * from users where email = '{}'").format(email)
           if len(result) > 0:
               return False, None
           else:
               return True, None
        except:
            return False, DATABASE_ERROR

    def insert_user(self, email, password, fullname, db=self.connection):
        cur = db.cursor()
        try:
            cur.execute("insert into users values()").format(email, password, fullname)
        except:
