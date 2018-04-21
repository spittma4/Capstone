# Jason Penza
# Hayden Knapp
# reddit_api

import praw
import random
import time


class redditApi:
    def __init__(self):
        pass

    reddits = {}
    def get_authen_url(self, email, client_id, client_secret):
        reddit = praw.Reddit(client_id=client_id.strip(), client_secret=client_secret.strip(), redirect_uri='http://ksusocialsuite.site/redditredirect', user_agent='ksu_social_suite')
        state = str(int(random.random() * 999999999))

        scopes = ['creddits', 'edit', 'flair', 'history', 'identity',
                              'modconfig', 'modcontributors', 'modflair', 'modlog',
                              'modothers', 'modposts', 'modself', 'modwiki',
                              'mysubreddits', 'privatemessages', 'read', 'report',
                              'save', 'submit', 'subscribe', 'vote', 'wikiedit',
                              'wikiread']

        url = reddit.auth.url(scopes, state, 'permanent')
        self.reddits[email] = reddit;
        return url

    def get_authorize(self, email, code):
        reddit = self.reddits[email]
        return reddit.auth.authorize(code)

    def post(self, subreddit, client_id, client_secret, refresh_token, title, contents):
        agent = "KSU_Social_Suite"
        reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, refresh_token = refresh_token,  user_agent = agent)
        sr = reddit.subreddit(subreddit)
        sr.submit(title, contents)

    def get_name(self, client_id, client_secret, refresh_token):
        agent = "KSU_Social_Suite"
        reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, refresh_token = refresh_token,  user_agent = agent)
        return reddit.user.me()

