# -*- coding:utf8 -*-
import json
from bottle import route, run, template, view
from bottle import HTTPResponse


def view_json(func):
    def _view_json(*args, **kwargs):
        resp = func(*args, **kwargs)
        body = json.dumps(resp)
        r = HTTPResponse(status=200, body=body)
        r.set_header('Content-Type', 'application/json')
        return r
    return _view_json


@route('/')
@view('index.html')
def index():
    """Render index page object
    """
    return {}


@route('/<asp>')
@view_json
def fetch_asp(asp):
    """
    """
    return []


run(host='localhost', port=8080)
