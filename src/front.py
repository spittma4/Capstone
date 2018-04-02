from bottle import template, run, route, get, post, redirect, request, response, static_file
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
        redirect('/login')
    if cookie:
        return _logins[cookie]
    else:
        redirect('/login')
        
# Static Routes --------------------------------------------#
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css/")

@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/font/")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img/")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js/")

#------------------------------------------------------------#

@route('/login')
def login(status=''):
    status = request.params.get("status")
    return template('login', status=status)

@route('/')
def root():
    get_session()
    redirect('/home')

@route('/home')
def home():
    username = get_session()

    return template('home', username=get_session())

@route('/signup')
def signup():
    status = request.params.get("status")
    if status == None:
        status = ''
    return template('signup', status=status)


@post('/auth')
def auth():
    username = request.forms.get("username")
    password = request.forms.get("password")

    if _coreKSU.check_login(username, password):
        add_session(username)

        redirect('/home')
    else:
        redirect('/login?status=fail')

@post('/adduser')
def adduser():
    username = request.forms.get("username")
    password = request.forms.get("password")
    fullname = request.forms.get("fullname")

    res, code =_coreKSU.sign_up(username, password, fullname)
    if res:
        redirect('/login')
    else:
        if code == _coreKSU.USER_EXISTS:
            status = 'User already exists.'
        else:
            status = 'Error processing request.'
        redirect('/signup?status={}'.format(status))

@route('/signout')
def signout():
    cookie = request.get_cookie("userCookie")
    _logins.pop(cookie)
    redirect('/')

@route('/twitter')
def twitter():
    twitterlink = ''
    username = get_session()
    pendingTwitter = not _coreKSU.twitter_hasAccount(username)
    ntweets = ''
    tweets = ''
    ntweets = request.params.count
    if ntweets == '':
        ntweets = 5
    else:
        ntweets = int(ntweets)
    if pendingTwitter:
        twitterlink = _coreKSU.twitter_getAuthLink(username)
    else:
        tweets = _coreKSU.twitter_getTweetsN(username, ntweets)
    return template('twitter', tweets=tweets, twitterlink=twitterlink, pendingTwitter=pendingTwitter)

@post('/inserttwitter')
def inserttwitter():
    username = get_session()
    pin = request.forms.get("pin")
    _coreKSU.twitter_addTwitterInfo(username, pin)

@post('/tweet')
def tweet():
    username = get_session()
    text = request.forms.text
    _coreKSU.twitter_postTweet(username, text)
    redirect('/twitter')

run(host='0.0.0.0', port=8080)

