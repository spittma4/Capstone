string = 'hello/friend/login/styles.css'

while '/' in string:
    string = string[string.index('/') + 1:]

