# Hayden Knapp
# Jason Penza
# Sam Pittman
# Jack Dauphars
# Stuart Mckaige

from database.database import Database
from database.mongoDB import Mongo
from social_media.twitter import twitter_api
from social_media.reddit import reddit_api

class Core:
    db = None
    twitter = None
    reddit = None
    mongo = None

    def __init__(self):
        self.db = Database()
        self.twitter = twitter_api.twitterApi()
        self.reddit = reddit_api.redditApi()

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
        access_token, access_token_secret, twitterName = self.twitter.get_userAccess(pin, email)
        self.db.add_twitter(twitterName, access_token, access_token_secret, email)

    def twitter_getTweetsN(self, email, n):
        twitterName, code = self.db.fetch_twittername(email)
        access, code = self.db.fetch_twitter(email, twitterName)
        tweets = self.twitter.get_tweets_since(access[1], access[2], twitterName, None, n)
        return tweets

    def get_twitterName(self, email):
        name, code = self.db.fetch_twittername(email)
        return name

    # post a tweet for a user
    def twitter_postTweet(self, email, contents):
        twitterName, code = self.db.fetch_twittername(email)
        mongoInstance = Mongo(email, contents)
        access, code = self.db.fetch_twitter(email, twitterName)
        self.twitter.tweet(access[1], access[2], contents)

    def twitter_hasAccount(self, email):
        res = self.db.fetch_twittername(email)
        if res[0] == 'None':
            return False
        return True

    # Reddit
    def get_reddit_authen_url(self, email, client_id, client_secret):
        return self.reddit.get_authen_url(email, client_id, client_secret)

    def reddit_authorize(self, email, code):
        return self.reddit.get_authorize(email, code)

    def reddit_save_three(self, email, client_id, client_secret, refresh_token):
        self.db.add_reddit(email, client_id, client_secret, refresh_token, email)

    def reddit_post(self, email, subreddit, title, contents):
        stuff = self.db.fetch_reddit(email, email)
        stuff = stuff[0]
        mongoInstance = Mongo(email, contents)
        self.reddit.post(subreddit, stuff[1], stuff[2], stuff[3], title, contents)

