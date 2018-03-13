from bottle import template, run, route, get, post, redirect, request, response
import uuid

import core

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
    if cookie not in _logins:
        redirect('/login/initial')
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

    return template('home', username=get_session())

@route('/signup/<status>')
def signup(status):
    return(template('signup', status=status))


@post('/auth')
def auth():
    username = request.forms.get("username")
    password = request.forms.get("password")

    if _coreKSU.check_login(username, password):
        add_session(username)

        redirect('/home')
    else:
        redirect('/login/fail')

@post('/adduser')
def adduser():
    username = request.forms.get("username")
    password = request.forms.get("password")
    fullname = request.forms.get("fullname")

    res, code =_coreKSU.sign_up(username, password, fullname)
    if res:
        redirect('/login/initial')
    else:
        if code == _coreKSU.USER_EXISTS:
            message = 'User already exists.'
        else:
            message = 'Error processing request.'
        redirect('/signup/{}'.format(message))

@route('/signout')
def signout():
    cookie = request.get_cookie("userCookie")
    _logins.pop(cookie)
    redirect('/')
    

run(host='0.0.0.0', port=80)

