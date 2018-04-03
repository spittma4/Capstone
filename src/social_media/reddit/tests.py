import unittest
import time
import random

import reddit_api

class redditTests(unittest.TestCase):
    def test_000_get_authent_link(self):
        print('https://www.reddit.com/prefs/apps/')
        reddit = reddit_api.redditApi()
        client_id = input("Enter the id ")
        client_secret = input("Enter the secret ")
        print(reddit.get_authen_url(client_id, client_secret))

if __name__ == '__main__':
    unittest.main(verbosity=2)
