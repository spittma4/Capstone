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
		statuses_resource_url = 'https://api.twitter.com/1.1/statuses/update.json?status={}'
		tweetContents = urllib.parse.quote_plus(tweetContents)
		consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
		access = oauth2.Token(accessToken, accessTokenSecret)
		client = oauth2.Client(consumer, access)

		part = ''
		username = ''
		lastTweetId = ''
		for character in tweetContents:
			if len(part) >= self.MAX_TWEET_LENGTH - len(username):
				if len(lastTweetId) > 0:
					response, data = client.request(statuses_resource_url.format(part) + '&in_reply_to_status_id={}'.format(lastTweetId), "POST")
				else:
					response, data = client.request(statuses_resource_url.format(part), "POST")
				print("response", response)
				print("data", data)
				data = json.loads(data)
				#for dat in data:
				#	print(dat)
				#username = data['user']['screen_name'] + '%20'
				lastTweetId = data['id_str']
				#part = '' + username
				part = '' 
			part += character

		if len(part) > 0:
			response, data = client.request(statuses_resource_url.format(part) + '&in_reply_to_status_id={}'.format(lastTweetId), "POST")

	def get_tweets_since(self, accessToken, accessTokenSecret, twitter_name, last_stored_id=None):
		resource_url = 'https://api.twitter.com/1.1/search/tweets.json'
		resource_url += '?q=' + urllib.parse.quote_plus(twitter_name) + '&tweet_mode=extended'
		if last_stored_id != None:
			resource_url += '&since_id={}'.format(last_stored_id)
		consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
	#	access = oauth2.Token(accessToken, accessTokenSecret)
		client = oauth2.Client(consumer)
		response, data = client.request(resource_url)
		data = json.loads(data)
		tweets = data['statuses']
		for tweet in tweets:
			print(tweet['full_text'])
	
	# get replies to a tweet up to a given id
	def get_replies(self, tweet_id, last_stored_id = None):
		pass

	request_tokens = {}

	def pending_access(self, twitter_name):
		return twitter_name in request_tokens

	def get_signUpUrl(self, twitter_name): 
		resource_url = 'https://api.twitter.com/oauth/request_token?x_auth_access_type=write&oauth_callback=oob'
		authorize_url = 'https://api.twitter.com/oauth/authorize?oauth_token={token}'
		consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
		client = oauth2.Client(consumer)
		response, data = client.request(resource_url)
		data = dict(urllib.parse.parse_qsl(data.decode("utf-8")))
		self.request_tokens[twitter_name] = (data['oauth_token'], data['oauth_token_secret'])
		return authorize_url.format(token=data['oauth_token'])

	def get_userAccess(self, pin, twitter_name):
		access_token_url = 'https://api.twitter.com/oauth/access_token'
		token = oauth2.Token(self.request_tokens[twitter_name][0], self.request_tokens[twitter_name][1])
		token.set_verifier(pin)
		consumer = oauth2.Consumer(private.CONSUMER_KEY, private.CONSUMER_SECRET)
		client = oauth2.Client(consumer, token)
		response, data = client.request(access_token_url, "POST")
		access_token = dict(urllib.parse.parse_qsl(data.decode('utf-8')))

		print("token: {}, secret: {}".format(access_token['oauth_token'], access_token['oauth_token_secret']))
		return access_token['oauth_token'], access_token['oauth_token_secret']
