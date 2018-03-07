#Jack
#Stuart

import string
import pymysql
import hashlib
import random

DB_PATH = "localhost"
DATABASE_ERROR = 1
PASSWORD_MISMATCH = 2
class Database:
    connection=None
    def __init__(self):
        self.connection = pymysql.connect(host=DB_PATH, user="root", database="prod")

    def generate_salt(self):
        salt = ""
        for i in range(0,15):
            salt+=random.choice(string.ascii_letters)
        return salt

    def get_salt(email, db=None):
        if (db==None):
            db = self.connection
        cursor = db.connection.cursor()
        try:
            salt = cursor.fetchall("select salt from users where email == {}".format(email))
            return True, salt
        except:
            return False, DATABASE_ERROR
        
    
    def check_login(self, email, password, db=None):
        if (db==None):
            db = self.connection
        if user_exists(email):
            result, code = verify_password(email, password)
            if result:
                return True, None
            else:
                return False, code
            
    def verify_password(email, password, db=None):
        if (db==None):
            db = self.connection
        result, salt = get_salt()
        if not result:
            return False, DATABASE_ERROR
        password += salt
        hashed = (hashlib.sha256(password.encode('ascii'))).hexdigest()
        
        cursor = db.connection.cursor()
        try:
            dbPassword = cursor.fetchall("select password from users where email == {}".format(email))
            if (dbPassword == hashed):
                return True, None
            else:
                return False, PASSWORD_MISMATCH
        except:
            return False, DATABASE_ERROR
        
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

        salt = self.generate_salt()
        hashed = hashlib.sha256(password.encode('ascii'))
        password = hashed.hexdigest()
        
        cur = db.cursor()
        print('yo')
        try:
            print('yo')
            cur.execute("insert into users values('{}', '{}', '{}', '{}')").format(email, password, fullname, salt)
            db.commit()
            #cur.execute("insert into users (email, salt, hash, twitter) values('{}', '{}', '{}', '{}')").format(email, password, fullname, salt)
            return True, None
        except:
            print('except')
            return False, DATABASE_ERROR
