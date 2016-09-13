# -*- coding:utf8 -*-
from bottle import route, run, template, view


@route('/')
@view('index.html')
def index():
    return {}


@route('/hello/<name>')
def ips(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)
