import sys, os
import praw
import authent
reddit = praw.Reddit(client_id='6vkAnnFdRTWXBw',
                     client_secret='dqZVH2dmijBkUHfc6S1ZAA-gMFE',
                     refresh_token='19117588746-VnRd3xKos0Z5z1ZbfrMLzpoj1aI',
                     user_agent='testscript by /u/ksusocial')
#print(reddit.auth.scopes()) -- shows what access we have to certain account
#reddit.subreddit('some_subreddit').submit('Some title', url='https://example.com').mod.distinguish(sticky=True)
client_subred=input('Which subreddit would you like to post to?:' )
subreddit = reddit.subreddit(client_subred)
hot_python = subreddit.hot(limit=3)
#for submission in hot_python:
    #print(dir(submission))
    #print(submission.title) #printing title of 5 hottest submission in subreddit Python

#if I wanted nonsticky subreddits
subreddit.submit('Test','Test') #-testing posting in a subreddit python with no text
print('Post a success')
'''for submission in hot_python:
    if not submission.stickied:
        print(submission.title) #title is an attribute, submission is a directory
	#comments
        comments=submission.comments.list() #.list 
        for comment in comments:
            print(20*'-')
            print(comment.body)'''
            #if len(comment.replies) > 0:
             #   for reply in comment.replies:
              #      print('REPLY'reply.body)    getting the reply body and displaying


#subreddit.subscribe()
