##Jason Penza
##reddit_api

#import reddit

import praw
import random
import time


class redditApi:
    def __init__(self):
        pass

    reddits = {}
    def get_authen_url(self, client_id, client_secret):
        reddit = praw.Reddit(client_id=client_id.strip(), client_secret=client_secret.strip(), redirect_uri='http://ksusocialsuite.site:8080/redditredirect', user_agent='ksu_social_suite')
        state = str(int(random.random() * 999999))

        scopes = ['creddits', 'edit', 'flair', 'history', 'identity',
                              'modconfig', 'modcontributors', 'modflair', 'modlog',
                              'modothers', 'modposts', 'modself', 'modwiki',
                              'mysubreddits', 'privatemessages', 'read', 'report',
                              'save', 'submit', 'subscribe', 'vote', 'wikiedit',
                              'wikiread']

        url = reddit.auth.url(scopes, state, 'permanent')
        return url


