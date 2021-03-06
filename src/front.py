from bottle import template, run, route, get, post, redirect, request, response, static_file
import uuid
import time

import core

_coreKSU = core.Core()

_logins = {}

_redditInfo = {}

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
    redditCode = request.params.reddit
    redditMessage = ''
    if '1' == redditCode:
        redditMessage = 'You cannot post to reddit at this time. Please wait.'
    redditAndTwitter = _coreKSU.reddit_hasAccount(username) and _coreKSU.twitter_hasAccount(username)
    print(redditAndTwitter)
    return template('home', username=get_session(), redditMessage = redditMessage, redditAndTwitter = redditAndTwitter)

@route('/signup')
def signup():
    status = request.params.get("status")
    if status == None:
        status = ''
    return template('signup', status=status)

@route('/about')
def about():
    username = get_session()

    return template('about', username=get_session())

@route('/analytics')
def about():
    username = get_session()
    data=_coreKSU.analytics_run(username)
    #data = {'anger': 0.0355845, 'analytical': 0.0758248125, 'sadness': 0.040780375, 'confident': 0.03621475, 'tentative': 0.155517625, 'joy': 0.061957875}
    print(data)
    for key in data:
        data[key] = round(data[key], 4)
    return template('contact', username=get_session(), data = data)

@route('/settings')
def about():
    username = get_session()

    return template('settings', username=get_session())

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
    twitterName = _coreKSU.get_twitterName(username)
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
    return template('twitter', tweets=tweets, twitterlink=twitterlink, pendingTwitter=pendingTwitter, username=get_session(), twitterName=twitterName)

@post('/inserttwitter')
def inserttwitter():
    username = get_session()
    pin = request.forms.get("pin")
    _coreKSU.twitter_addTwitterInfo(username, pin)
    redirect('/twitter')

@post('/tweet')
def tweet():
    username = get_session()
    text = request.forms.text
    _coreKSU.twitter_postTweet(username, text)
    redirect('/twitter')

@route('/reddit')
def reddit():
    username = get_session()
    redditlink = ''
    pendingReddit = not _coreKSU.reddit_hasAccount(username)
    return template('reddit', username=get_session(), redditlink=redditlink, pendingReddit=pendingReddit, redditName=_coreKSU.reddit_getName(username))

@route('/addreddit')
def addreddit():
    username = get_session()
    return template('addreddit', username=get_session())

@post('/redditurl')
def redditurl():
    username = get_session()
    _redditInfo[username] = (request.forms.id.strip(), request.forms.secret.strip())
    redirect(_coreKSU.get_reddit_authen_url(username, request.forms.id, request.forms.secret))

@route('/redditredirect')
def redditredirect():
    username = get_session()
    code = request.params.code
    thing = _coreKSU.reddit_authorize(username, code)
    _coreKSU.reddit_save_three(username, _redditInfo[username][0], _redditInfo[username][1], thing)
    redirect('/reddit')

@post('/redditpost')
def addreddit():
    username = get_session()
    subreddit = request.forms.subreddit.strip()
    title = request.forms.title
    contents = request.forms.contents
    res = _coreKSU.reddit_post(username, subreddit, title, contents)
    if not res:
        redirect('/home?reddit=1')
    redirect('/reddit')

@post('/postall')
def addreddit():
    username = get_session()
    subreddit = request.forms.subreddit.strip()
    title = request.forms.title
    contents = request.forms.contents
    res = _coreKSU.reddit_post(username, subreddit, title, contents)
    if not res:
        redirect('/home?reddit=1')
    _coreKSU.twitter_postTweet(username, contents)
    redirect('/home')

run(host='0.0.0.0', port=80)
