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

    def generate_salt(self):
        salt = ""
        for i in range(0,15):
            salt+=random.choice(string.letters)
        return salt

    """Alledgedy this will just work thru pymysql when we execute a command
    def sanitize(self, inString):
        #result =
        pass
    """
    def check_login(self, email, password, db=None):
        pass

    def user_exists(self, email, db=None):
        if(db==None):
            db=self.connection
        cur = db.connection.cursor()
        try:
           result = cur.fetchall("select * from users where email = '{}'").format(email)
           if len(result) > 0:
               return False, None
           else:
               return True, None
        except:
            return False, DATABASE_ERROR

    def insert_user(self, email, password, fullname, db=None):
        if(db==None):
            db=self.connection
        cur = db.cursor()
        try:
            cur.execute("insert into users values()").format(email, password, fullname)
            return True, None
        except:
            return False, DATABASE_ERROR
