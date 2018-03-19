# Hayden Knapp
# Jason Penza
# Sam Pittman
# Jack Dauphars
# Stuart Mckaige

from database.database import Database
from social_media.twitter import twitter_api

class Core:
    db = None
    twitter = None

    def __init__(self):
        self.db = Database()
        self.twitter = twitter_api.twitterApi()

####################################################################################
    # user functions

    # return a bool indicating whether credentials were correct or not
    def check_login(self, email, password):
        res, code = self.db.check_login(email, password)
        if res:
            return True

    # add a user, returns
    # Given: password is sufficient
    # returns true or false
    USER_EXISTS = 1
    INVALID_EMAIL = 2
    DATABASE_FAILURE = 3
    def sign_up(self, email, password, fullname):
        # check if email is duplicate
        res, code = self.db.user_exists(email)
        if res:
            return False, self.USER_EXISTS

        # add the user
        else:
            res, code = self.db.insert_user(email, password, fullname)
            if not res:
                return False, self.DATABASE_FAILURE
            else:
                return True, 0
        

####################################################################################
    # social media functions
    # Twitter

    # returns the link the user will be redirected to
    def twitter_getAuthLink(self, email):
        return self.twitter.get_signUpUrl(email)

    # takes the users key and adds oauth info to the db
    def twitter_addTwitterInfo(self, email, pin):
        access_token, access_token_secret = self.twitter.get_userAccess(pin, email)
        twitterName = 'hknapp4ksu'
        self.db.add_twitter(twitterName, access_token, access_token_secret, email)

    # get a users last tweets in the day range as a list
    # dates are mm-dd-yyyy
    def twitter_getTweetsRange(self, email, startDay, endDay):
        pass

    def twitter_getTweetsN(self, email, n):
        twitterName, code = self.db.fetch_twittername(email)
        access, code = self.db.fetch_twitter(email, twitterName)
        tweets = self.twitter.get_tweets_since(access[1], access[2], twitterName, None, n)
        return tweets

    # post a tweet for a user
    def twitter_postTweet(self, email, contents):
        twitterName, code = self.db.fetch_twittername(email)
        access, code = self.db.fetch_twitter(email, twitterName)
        self.twitter.tweet(access[1], access[2], contents)

    def twitter_hasAccount(self, email):
        res = self.db.fetch_twittername(email)
        if res[0] == 'None':
            return False
        return True
