import praw
import random
import time
from bottle import run, route, request

#r = None
#print("id: ", id(r))

@route('/')
def redditauth():
        print("id: ", id(r))
        code = request.params.code
        return r.auth.authorize(code)

if __name__ == '__main__':
        print('https://www.reddit.com/prefs/apps/')

        random.seed(time.time())

        client_id = input("Enter first thing")
        client_secret = input("Enter second thing")
        global r
        r = praw.Reddit(client_id=client_id.strip(), client_secret=client_secret.strip(), redirect_uri='http://localhost:8080', user_agent='praw_refresh_token_example')
        print("id: ", id(r))
        state = str(int(random.random() * 100000))

        scopes = ['creddits', 'edit', 'flair', 'history', 'identity',
                          'modconfig', 'modcontributors', 'modflair', 'modlog',
                          'modothers', 'modposts', 'modself', 'modwiki',
                          'mysubreddits', 'privatemessages', 'read', 'report',
                          'save', 'submit', 'subscribe', 'vote', 'wikiedit',
                          'wikiread']

        url = r.auth.url(scopes, state, 'permanent')

        print('Go here: ' + url)

        run(host='0.0.0.0', port=8080)
