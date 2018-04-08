# Hayden Knapp
# Test the functionality of the Twitter API

import unittest
import random
import requests

import private
from twitter_api import twitterApi

class TestTwitterApi(unittest.TestCase):
    """
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

    def test_003_larger_random_tweet_owner(self):
        testApi = twitterApi()
        word = ''

        tweetLength = 700
        while len(word) < tweetLength:
            word += str(int(random.random() * 10))
        testApi.tweet(private.OWNER_ACCESS_TOKEN, private.OWNER_ACCESS_TOKEN_SECRET, word)

        twitterPage = requests.get('https://twitter.com/hknapp4ksu')
        total = 0
        nSamples = 50
        segmentLength = 8
        for i in range(nSamples):
            randLoc = int(random.random() * (tweetLength - segmentLength))
            segment = word[randLoc: randLoc + segmentLength]
            if word in twitterPage:
                total += 1
        self.assertGreaterEqual(total + 10, segmentLength)
    
    def test_004_larger_interject_tweet_owner(self):
        testApi = twitterApi()
        word =    I'd just like to interject for moment. What you're refering to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux!
        testApi.tweet(private.OWNER_ACCESS_TOKEN, private.OWNER_ACCESS_TOKEN_SECRET, word)

        twitterPage = requests.get('https://twitter.com/hknapp4ksu')
        total = 0
        nSamples = 50
        segmentLength = 8
        tweetLength = len(word)
        for i in range(nSamples):
            randLoc = int(random.random() * (tweetLength - segmentLength))
            segment = word[randLoc: randLoc + segmentLength]
            if word in twitterPage:
                total += 1
        self.assertGreaterEqual(total + 10, segmentLength)
    def test_005_get_tweets(self):
        testApi = twitterApi()
        results = testApi.get_tweets_since(private.OWNER_ACCESS_TOKEN, private.OWNER_ACCESS_TOKEN_SECRET, 'hknapp4ksu')
        for result in results:
            print(result)
    def test_006_get_auth_url(self):
        testApi = twitterApi()
        url = testApi.get_signUpUrl()
        print(url)
"""
    def test_007_get_tokens(self):
        testApi = twitterApi()
        url = testApi.get_signUpUrl('hknapp4ksu')
        print(url)
        pin = str(input("Enter pin: "))
        access_token, access_token_secret = testApi.get_userAccess(pin, 'hknapp4ksu')
        print("token: {}, secret: {}".format(access_token, access_token_secret))
if __name__ == '__main__':
    unittest.main(verbosity = 2)
