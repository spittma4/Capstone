from bottle import template, run, route, get, post, redirect, request, response
import uuid

import mock_core as core

_coreKSU = core.Core()

_logins = {}

#Function to set a cookie for a session
def add_session(username):
	cookie = str(uuid.uuid4())

	_logins[cookie] = username

	response.set_cookie("userCookie", cookie)

#Function to get a cookie once logged in
def get_session():
	cookie = request.get_cookie("userCookie")

	if cookie:
		return _logins[cookie]
	else:
		redirect('/login/initial')

@route('/login/<status>')
def login(status):
	return template('login', status=status)

@route('/')
def root():
	redirect('/login/initial')

@route('/home')
def home():
	username = get_session()

	return template('home')

@post('/auth')
def auth():
	username = request.forms.get("username")
	password = request.forms.get("password")

	if _coreKSU.check_login(username, password):
		add_session(username)

		redirect('/home')
	else:
		redirect('/login/fail')



run()

