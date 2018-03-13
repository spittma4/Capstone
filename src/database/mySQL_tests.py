#stuart
#jack
from database import Database
import pymysql
import unittest
DB_PATH = "localhost"

def create_database(connection):
    cur = connection.cursor()
    cur.execute("""CREATE TABLE twitter (username varchar(100) PRIMARY KEY, access varchar(50), access_secret varchar(50))""")
    cur.execute("""CREATE TABLE reddit (username varchar(100) PRIMARY KEY, access varchar(50), access_secret varchar(50))""")
    cur.execute("""CREATE TABLE users (email varchar(100),salt varchar(100),hash varchar(100),fullname varchar(100),twittername varchar(100),redditname varchar(100), instagramname varchar(100),foreign key (twittername) references twitter(username),foreign key (redditname) references reddit(username))""")

def get_connection():
    connection = pymysql.connect(host=DB_PATH, user="root", database="prod")
    return connection

def tear_down_database(con):
    cur = con.cursor()
    cur.execute("DROP TABLE reddit")
    cur.execute("DROP TABLE twitter")
    cur.execute("DROP TABLE users")
    
if __name__ == "__main__" :
    con=get_connection()
    #create_database(con)
    db = Database()
    res, code =db.insert_user("jim@school.com", "doggie", "Jim James",con )
    print(res, code)
    #print(db.check_login("jim@school.com", "doggie"))
    res, code = db.add_twitter("jjames", "token","speshul secrets", "jim@school.com", con)
    print(res, code)
    res, code = db.add_reddit("leddituser", "token","speshul secrets", "jim@school.com", con)
    print(res,code)
    #tear_down_database(con)
