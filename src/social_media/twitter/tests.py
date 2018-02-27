# Hayden Knapp
# Test the functionality of the Twitter API

import unittest
import random
import requests

import private
from twitter_api import twitterApi

class TestTwitterApi(unittest.TestCase):
	def test_001_dependencies_installed(self):
		pass

	def test_002_small_random_tweet_owner(self):
		testApi = twitterApi()
		word = ''
		while len(word) < 100:
			word += str(int(random.random() * 10))
		testApi.tweet(private.OWNER_ACCESS_TOKEN, private.OWNER_ACCESS_TOKEN_SECRET, word)
		twitterPage = requests.get('https://twitter.com/hknapp4ksu')
		self.assertEqual(word in twitterPage.text, True)

	def test_002_small_random_tweet_owner(self):
		testApi = twitterApi()
		word = ''
		while len(word) < 500:
			word += str(int(random.random() * 10))
		testApi.tweet(private.OWNER_ACCESS_TOKEN, private.OWNER_ACCESS_TOKEN_SECRET, word)
		twitterPage = requests.get('https://twitter.com/hknapp4ksu')
		self.assertEqual(word in twitterPage.text, True)


if __name__ == '__main__':
	unittest.main(verbosity = 2)
