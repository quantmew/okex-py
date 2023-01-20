import hmac
import base64
import time
import datetime
from typing import Iterable
from . import consts as c

from enum import Enum

def enum_to_str(e):
    if isinstance(e, Enum):
        return e.value
    else:
        return e

def iterable_to_str(l):
    ret = ''
    for i, v in enumerate(l):
        if i == 0:
            ret += v
        else:
            ret += ',' + v
    
    return ret

def to_list(l):
    if isinstance(l, Iterable):
        return list(l)
    else:
        return [l]

def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body


def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.OK_ACCESS_KEY] = api_key
    header[c.OK_ACCESS_SIGN] = sign
    header[c.OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[c.OK_ACCESS_PASSPHRASE] = passphrase

    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def get_timestamp() -> str:
    now = datetime.datetime.utcnow()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

def get_local_timestamp() -> int:
    return int(time.time())

def signature(timestamp, method: str, request_path: str, body, secret_key: str):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)
