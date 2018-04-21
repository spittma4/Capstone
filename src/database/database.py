#Jack
#Stuart

from . import private
import string
import pymysql
import hashlib
import random

DB_PATH = "localhost"
DATABASE_ERROR = 1
PASSWORD_MISMATCH = 2
USER_DOES_NOT_EXIST = 3

class Database:
    connection=None
    def __init__(self):
        print(private.password)
        self.connection = pymysql.connect(host=DB_PATH, user="root", password=private.password, database="prod")

    def generate_salt(self):
        salt = ""
        for i in range(0,15):
            salt+=random.choice(string.ascii_letters)
        return salt

    def get_salt(self, email, db=None):
        if (db==None):
            db = self.connection
        cursor = db.cursor()
        try:
            cursor.execute("select salt from users where email = '{}'".format(email))
            salt = cursor.fetchone()
            return True, salt
        except:
            return False, DATABASE_ERROR
        
    
    def check_login(self, email, password, db=None):
        if (db==None):
            db = self.connection
        result,code = self.user_exists(email)
        if result:
            result, code = self.verify_password(email, password)
            if result:
                return True, True
            else:
                return False, code
        return False, False
            
    def verify_password(self, email, password, db=None):
        if (db==None):
            db = self.connection
        result, salt = self.get_salt(email)
        if not result:
            return False, DATABASE_ERROR
        password += salt[0]
        hashed = hashlib.sha256(password.encode('ascii'))
        hashed = hashed.hexdigest()
        cursor = db.cursor()
        try:
            cursor.execute("select hash from users where email = '{}'".format(email))
            dbPassword = cursor.fetchall()
            dbPassword = dbPassword[0][0]
            if (dbPassword == hashed):
                return True, None
            else:
                return False, PASSWORD_MISMATCH
        except:
            return False, DATABASE_ERROR
        
    def user_exists(self, email, db=None):
        if(db==None):
            db=self.connection
        cur = db.cursor()
        try:
           cur.execute("select * from users where email = '{}'".format(email))
           result = cur.fetchall()
           if len(result) > 0:
               return True, None
           else:
               return False, USER_DOES_NOT_EXIST
        except:
            return False, DATABASE_ERROR

    def insert_user(self, email, password, fullname, db=None):
        if(db==None):
            db=self.connection

        salt = self.generate_salt()
        password += salt
        hashed = hashlib.sha256(password.encode('ascii'))
        password = hashed.hexdigest()
        cur = db.cursor()
        try:
            cur.execute("insert into users values('{}', '{}', '{}', '{}',NULL,NULL,NULL)".format(email, salt, password, fullname))
            db.commit()
            #cur.execute("insert into users (email, salt, hash, twitter) values('{}', '{}', '{}', '{}')").format(email, password, fullname, salt)
            return True, None
        except:
            return False, DATABASE_ERROR
            
    def fetch_fullname(self, email, db=None):
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""
            SELECT * 
            FROM users as u
            WHERE u.email = '{}'      
            """.format(
                email
            ))
            result = cur.fetchall()
            result = str(result[0][3])
            return result, None
        except:
            return False, DATABASE_ERROR


    def add_twitter(self, username, access, access_secret, email, db=None):
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""INSERT INTO twitter (
            username,
            access,
            access_secret
            ) VALUES (
            '{}',
            '{}',
            '{}'
            )
            """.format(
                username,
                access,
                access_secret
            ))
            cur.execute("""UPDATE users SET 
            twittername ='{}'
            WHERE
            email = '{}'
            """.format(username, email)
            )
            db.commit()
            return True, None
        except:
            return False, DATABASE_ERROR

    def fetch_twitter(self, email, username, db=None):
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""
            SELECT * 
            FROM twitter as t
            JOIN users as u
            WHERE u.twittername = '{}'
            AND u.email = '{}'      
            """.format(
                username,
                email
            ))
            result = cur.fetchall()
            result = tuple([result[0][0],result[0][1],result[0][2]])
            return result, None
        except:
            return False, DATABASE_ERROR

    def fetch_twittername(self, email, db=None):
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""
            SELECT * 
            FROM users as u
            WHERE u.email = '{}'      
            """.format(
                email
            ))
            result = cur.fetchall()
            result = str(result[0][4])
            return result, None
        except:
            return False, DATABASE_ERROR


    def add_reddit(self, username, access, access_secret, refresh_token, email, db=None):
        #print(username, access, access_secret, refresh_token, email)
        print("Reddit username to be added: {}".format(username))
        print("Email to be added: {}".format(email))
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""INSERT INTO reddit (
            username,
            access,
            access_secret,            
            refresh_token
            ) VALUES (
            '{}',
            '{}',
            '{}',
            '{}'
            )
            """.format(
                username,
                access,
                access_secret,
                refresh_token
            ))
            cur.execute("""UPDATE users SET 
            redditname ='{}'
            WHERE
            email = '{}'
            """.format(
                username,
                email
            ))
            db.commit()
            return True, None
        except:
            return False, DATABASE_ERROR

    def fetch_redditname(self, email, db=None):
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""
            SELECT * 
            FROM users as u
            WHERE u.email = '{}'      
            """.format(
                email
            ))
            result = cur.fetchall()
            result = str(result[0][5])
            print("result in fetch_redditname: ",result)
            return result, None
        except:
            return False, DATABASE_ERROR
    
    def fetch_reddit(self, email, username, db=None):
        if(db==None):
            db=self.connection

        cur = db.cursor()
        try:
            cur.execute("""
            SELECT * 
            FROM reddit as r
            JOIN users as u
            WHERE u.redditname = '{}'
            AND u.email = '{}'      
            """.format(
                username,
                email
            ))
            result = cur.fetchall()
            result = tuple([result[0][0],result[0][1],result[0][2], result[0][3]])
            print("result in fetch_reddit: ", result)
            return result, None
        except:
            return False, DATABASE_ERROR
