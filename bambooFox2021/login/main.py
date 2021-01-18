# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: ./main.py
# Compiled at: 2021-01-07 20:23:56
# Size of source mod 2**32: 2359 bytes
from os import getenv, urandom
from flask import Flask, g, request, session, send_file, render_template

app = Flask(__name__)


class Flag:

    def __str__(self):
        if session.get('is_admin', False):
            return getenv('FLAG', 'FLAG{F4K3_FL4G}')
        return u"Oops, You're not admin (\u30fb\u3078\u30fb)"


@app.route('/')
def index():
    session['is_admin'] = False
    return "hi"


@app.route('/hint')
def hint():
    filename = request.args.get('file')
    if filename.endswith('.py'):
        return 'Denied: *.py'
    return send_file(filename)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
