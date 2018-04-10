import unittest
import time
import random
from bottle import run, route, request

import reddit_api

@route('/redditredirect')
def index():
    global reddit
    code = request.params.code
    return reddit.get_authorize("hknapp4", code)

class redditTests(unittest.TestCase):
    def test_000_get_authent_link(self):
        global reddit
        print('https://www.reddit.com/prefs/apps/')
        reddit = reddit_api.redditApi()
        client_id = input("Enter the id ")
        client_secret = input("Enter the secret ")
        print(reddit.get_authen_url("hknapp4", client_id, client_secret))
        run(host="0.0.0.0", port=80)


if __name__ == '__main__':
    unittest.main(verbosity=2)
