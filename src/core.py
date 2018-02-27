# Hayden Knapp
# Jason Penza
# Sam Pittman
# Jack Dauphars
# Stuart Mckaige

class Core:
    db = None

    def __init__(self):
        pass

####################################################################################
    # user functions

    # return a bool indicating whether credentials were correct or not
    def check_login(self, username, password):
        pass

    # add a user, returns
    # Given: password is sufficient
    # returns true or false

    USER_EXISTS = 1
    INTERNAL_ERROR = 2

    def sign_up(self, email, password, fullname):
        # check if email is duplicate
        if db.user_exists(username):
            return False, USER_EXISTS

####################################################################################
    # social media functions
    def 

    # Twitter

    # returns the link the user will be redirected to
    def twitter_getAuthLink(self, ksuusername):
        pass

    # takes the users key and adds oauth info to the db
    def twitter_addTwitterInfo(self, ksuusername, twitterNumber):
        pass

    # get a users last tweets in the day range as a list
    # dates are mm-dd-yyyy
    def twitter_getTweetsRange(self, ksuusername, startDay, endDay):
        pass

    # post a tweet for a user
    def 
