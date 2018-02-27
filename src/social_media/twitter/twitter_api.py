# Hayden Knapp

import twitter

import private

class twitterApi:
	def __init__(self):
		pass

	def tweet(self, accessToken, accessTokenSecret, tweetContents):
		t = twitter.Twitter(auth = twitter.OAuth(accessToken, accessTokenSecret, private.CONSUMER_KEY, private.CONSUMER_SECRET))
		t.statuses.update(status = tweetContents)
