# -*- coding:utf8 -*-
from urllib.request import urlopen
import json


def fetch_all_networks():
    resp = urlopen('https://api.github.com/meta')
    meta = json.loads(resp.read().decode('utf8'))
    return list(set(meta['hooks'] + meta['pages'] + meta['git']))
    
