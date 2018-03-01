# Hayden Knapp
# Jason Penza
# Sam Pittman
# Jack Dauphars
# Stuart Mckaige

import database

class Core:
	db = None

	def __init__(self):
		db = database.Database()

####################################################################################
	# user functions

	# return a bool indicating whether credentials were correct or not
	def check_login(self, email, password):
		return db.check_login(self, email, password)

	# add a user, returns
	# Given: password is sufficient
	# returns true or false
	USER_EXISTS = 1
	INVALID_EMAIL = 2
	DATABASE_FAILURE = 3
	def sign_up(self, email, password, fullname):
		if email != db.sanitize(email):
			return False, INVALID_EMAIL

		# check if email is duplicate
		if db.user_exists(email):
			return False, USER_EXISTS

		# add the user
		else:
			if not db.insert_user(email, password, fullname):
				return False, DATABASE_FAILURE
			else:
				return True, None
		

####################################################################################
	# social media functions
	def 

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
