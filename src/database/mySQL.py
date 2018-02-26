from pymysql import cursors.Cursor



def sanitize_input():
    return

def try_userName(cursor, givenName):

    
    cursor.exectute("SELECT * FROM socialSuiteUser WHERE email == %", givenName)

    return cursor
