# -*- coding:utf8 -*-
import sys
import os
import json
import argparse
import importlib
from bottle import route, run, template, view, HTTPResponse


def view_json(func):
    def _view_json(*args, **kwargs):
        resp = func(*args, **kwargs)
        if isinstance(resp, HTTPResponse):
            return resp
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
    try:
        module_fullpath = 'gateway.{}'.format(asp)
        module = importlib.import_module(module_fullpath)
    except ImportError:
        return HTTPResponse(status=404)
    return module.fetch_all_networks()


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # Declare argumetns
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', default='127.0.0.1')
    parser.add_argument('-P', '--port', default='8080')

    # Run server
    args = parser.parse_args(argv)
    sys.path.insert(0, os.path.dirname(__file__))
    run(host=args.host, port=args.port)


if __name__ == '__main__':
    main()    
