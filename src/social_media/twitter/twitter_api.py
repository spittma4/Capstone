# Hayden Knapp

import urllib
import json
import requests
import oauth2

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

#import private
from . import private

class twitterApi:
    def __init__(self):
        pass


    MAX_TWEET_LENGTH = 280
    def tweet(self, accessToken, accessTokenSecret, tweetContents):
        print("Hello from the tweet function!")
        print("Tweet contents: {}".format(tweetContents))
        print(accessToken, accessTokenSecret)
        statuses_resource_url = 'https://api.twitter.com/1.1/statuses/update.json?status={}'
        tweetContents = urllib.parse.quote_plus(tweetContents)
        consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
        access = oauth2.Token(accessToken, accessTokenSecret)
        client = oauth2.Client(consumer, access)

        part = ''
        username = ''
        lastTweetId = ''
        response, data = client.request(statuses_resource_url.format(tweetContents), "POST")
        """
        for character in tweetContents:
            if len(part) >= self.MAX_TWEET_LENGTH - len(username):
                if len(lastTweetId) > 0:
                    response, data = client.request(statuses_resource_url.format(part) + '&in_reply_to_status_id={}'.format(lastTweetId), "POST")
                    print("Hello from the tweet function!2")
                else:
                    response, data = client.request(statuses_resource_url.format(part), "POST")
                    print("Hello from the tweet function!1")
                    print(response)
                    print(data)
                data = json.loads(data)
                lastTweetId = data['id_str']
                part = '' 
            part += character

        if len(part) > 0:
            response, data = client.request(statuses_resource_url.format(part) + '&in_reply_to_status_id={}'.format(lastTweetId), "POST")
        """

    def get_tweets_since(self, accessToken, accessTokenSecret, twittername, last_stored_id=None, numberOfTweets=100):
        resource_url = 'https://api.twitter.com/1.1/search/tweets.json'
        resource_url += '?q=from:' + urllib.parse.quote_plus(twittername) + '&tweet_mode=extended&count=' + str(numberOfTweets)
        if last_stored_id != None:
            resource_url += '&since_id={}'.format(last_stored_id)
        consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
        client = oauth2.Client(consumer)
        response, data = client.request(resource_url)
        data = json.loads(data.decode())
        tweets = data['statuses']
        retTweets = []
        for tweet in tweets:
            retTweets.append((tweet['full_text'], tweet['favorite_count'], tweet['retweet_count']))
        return retTweets
            
    
    # get replies to a tweet up to a given id
    def get_replies(self, tweet_id, last_stored_id = None):
        pass

    request_tokens = {}

    def pending_access(self, email):
        return email in request_tokens

    def get_signUpUrl(self, email): 
        resource_url = 'https://api.twitter.com/oauth/request_token?x_auth_access_type=write&oauth_callback=oob'
        authorize_url = 'https://api.twitter.com/oauth/authorize?oauth_token={token}'
        consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
        client = oauth2.Client(consumer)
        response, data = client.request(resource_url)
        data = dict(urllib.parse.parse_qsl(data.decode("utf-8")))
        self.request_tokens[email] = (data['oauth_token'], data['oauth_token_secret'])
        return authorize_url.format(token=data['oauth_token'])

    def get_userAccess(self, pin, email):
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        token = oauth2.Token(self.request_tokens[email][0], self.request_tokens[email][1])
        token.set_verifier(pin)
        consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
        client = oauth2.Client(consumer, token)
        response, data = client.request(access_token_url, "POST")
        access_token = dict(urllib.parse.parse_qsl(data.decode('utf-8')))
        print("Response: ", response)
        print("Data: ", data)

        return access_token['oauth_token'], access_token['oauth_token_secret']
