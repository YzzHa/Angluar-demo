#coding=utf-8
from flask import Flask, request
from flask_cors import *  # 导入模块s
from books import books
from response import set_status
from db import dbconn

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.before_request
def before_request():
    con = dbconn.connection
    try:
        con.ping()
    except Exception as e:
        con.reconnect()
        print(e)

@app.after_request
def after_request(environ):
    set_status(environ.status_code, environ.status)
    return environ

app.register_blueprint(books, url_prefix='/books')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
