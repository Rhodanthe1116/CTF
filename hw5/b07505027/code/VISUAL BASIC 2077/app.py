#!/usr/bin/env python3
from os import getenv, urandom
from flask import Flask, g, request, session, send_file
import sqlite3

app = Flask(__name__)
app.secret_key = urandom(32)


class Flag():
    def __init__(self, flag):
        self.flag = flag
    def __str__(self):
        return self.flag if session.get('is_admin', False) else "Oops, You're not admin (・へ・)"


def db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('sqlite.db')
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    session['is_admin'] = False
    return send_file("index.html")

@app.route("/hint")
def hint():
    _='_=%r;return (_%%_)';return (_%_)

@app.route('/login', methods=["POST"])
def login():

    res_send = ''

    flag = Flag('flag{asdasd}')
    username = request.form.get('username', '')
    res_send += username + '<br/>'
    password = request.form.get('password', '')
    cursor = db().cursor()
    # query = f"select username, password from users where username='000' UNION SELECT {username} AS username, 2 AS password--' and password='{password}'"
    query = f"select username, password from users where username='{username}' and password='{password}'"
    res_send += '<br/>' +  query + '<br/><br/>'
    print(query)
    cursor.execute(query)
    res = cursor.fetchone()

    if  (res != None and res['username'] == username and res['password'] == password):
        return ("<h1>Hello, " + username + " ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡ </h1> Here is your flag: {flag} ").format(flag=flag)
    else:
        user = res
        # query = f"select username, password from users where username='000' UNION SELECT 1, 2 FROM users --"
        # cursor.execute(query)
        # res = cursor.fetchone()
        # resString = f'{res['username']} {res['password']}'
        for i in range(len(password)):
            if res['password'][i] != password[i]:
                res_send += f'different {i}: {res["password"][i]} vs {password[i]}' + '<br/>'

        res_send += f'''
            No (´;ω;`)  <br/>
            {res} \n<br/>
            username: {username} <br/>
            password: {password} <br/>
            res username: {res['username'] if user else''}  <br/>
            res password: {res['password'] if user else ''} <br/>

            pass res None? {res != None} <br/>
            pass username? {res['username'] == username} <br/>
            pass password? {res['password'] == password} <br/>

        '''
        res_send += ("<h1>Hello, " + username + "  </h1> Here is your flag: {flag} ").format(flag=flag)
        return res_send 


if __name__ == "__main__":
    app.run(port=5000)


'''
a'; INSERT INTO users (username, password) VALUES ('aaa', 'bbb');
'''