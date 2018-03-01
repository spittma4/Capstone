#stuar
from database import Database
import pymysql
import unittest
DB_PATH = "localhost"

def create_database():
    connection = pymysql.connect(host=DB_PATH, user="root", database="test")
    cur = connection.cursor()
    cur.execute("CREATE TABLE users (email varchar(100),salt varchar(100), hash varchar(100), twitter varchar(100))")
    #cur.execute("CREATE TABLE users (email varchar(25),salt varchar(15), hash varchar(64), twitter varchar(15))")
    return connection

def tear_down_database(con):
    cur = con.cursor()
    cur.execute("DROP TABLE users")

if __name__ == "__main__" :
    con=create_database()
    db = Database()
    db.insert_user("jim@school.com", "doggie", "Jim James",con )
    #tear_down_database(con)
