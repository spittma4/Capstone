# Hayden Knapp
# Jason Penza
# Sam Pittman
# Jack Dauphars
# Stuart Mckaige

#import database
import mockdb as database

class Core:
	db = None

	def __init__(self):
		db = database.Database()

####################################################################################
	# user functions

	# return a bool indicating whether credentials were correct or not
	def check_login(self, email, password):
            if email == 'spittma4' and password == 'password':
                return False

	# add a user, returns
	# Given: password is sufficient
	# returns true or false

####################################################################################
	# social media functions
#	def 

	# Twitter

	# returns the link the user will be redirected to
	def twitter_getAuthLink(self, email):
		pass

	# takes the users key and adds oauth info to the db
	def twitter_addTwitterInfo(self, email, twitterNumber):
		pass

	# get a users last tweets in the day range as a list
	# dates are mm-dd-yyyy
	def twitter_getTweetsRange(self, email, startDay, endDay):
		pass

	# post a tweet for a user
#	def 
