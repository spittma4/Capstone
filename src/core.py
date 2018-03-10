# Hayden Knapp
# Jason Penza
# Sam Pittman
# Jack Dauphars
# Stuart Mckaige

from database.database import Database

class Core:
    db = None

    def __init__(self):
        self.db = Database()

####################################################################################
    # user functions

    # return a bool indicating whether credentials were correct or not
    def check_login(self, email, password):
        print(email, password)
        return self.db.check_login(email, password)

    # add a user, returns
    # Given: password is sufficient
    # returns true or false
    USER_EXISTS = 1
    INVALID_EMAIL = 2
    DATABASE_FAILURE = 3
    def sign_up(self, email, password, fullname):
        print("in sign up function")
        # check if email is duplicate
        res, code = self.db.user_exists(email)
        if res:
            print("user exists")
        #    return False, self.USER_EXISTS

        # add the user
        else:
            res, code = self.db.insert_user(email, password, fullname)
            print(res, code)
            if not res:
                return False, self.DATABASE_FAILURE
            else:
                return True, 0
        

####################################################################################
    # social media functions
#    def 

    # Twitter

    # returns the link the user will be redirected to
    def twitter_getAuthLink(self, email):
        pass

    # takes the users key and adds oauth info to the db
    def twitter_addTwitterInfo(self, email, twitterNumber):
        pass

    # get a users last tweets in the day range as a list
    # dates are mm-dd-yyyy
    def twitter_getTweetsRange(self, email, startDay, endDay):
        pass

    # post a tweet for a user
#    def 
