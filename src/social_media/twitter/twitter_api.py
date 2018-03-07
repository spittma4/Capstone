# Hayden Knapp

import urllib
import json
import requests
import oauth2

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

import private

class twitterApi:
	def __init__(self):
		pass


	MAX_TWEET_LENGTH = 280
	def tweet(self, accessToken, accessTokenSecret, tweetContents):
		
		statuses_resource_url = 'https://api.twitter.com/1.1/statuses/update.json'
		#tweetContents = urllib.parse.quote_plus(tweetContents)
		#statuses_resource_url = statuses_resource_url + '?status=' + tweetContents
		consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
		access = oauth2.Token(accessToken, accessTokenSecret)
		client = oauth2.Client(consumer, access)

		splitTweet = []
		startPoint = 0
		while startPoint < tweetContents.length():
			 splitTweet.append(tweetContents[startPoint : startPoint + self.MAX_TWEET_LENGTH] if startPoint + self.MAX_TWEET_LENGTH < len(tweetContents) else tweetContents[startPoint : len(tweetContents))
			startPoint += self.MAX_TWEET_LENGTH

		print(tweetContents)
		print('\n\n\n\n')
		for e in splitTweet:
			print(e)

		#response, data = client.request(statuses_resource_url, "POST")

	def get_signUpUrl(self): 
		pass

	def get_userAccess(self):
		pass
