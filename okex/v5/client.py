import requests
import json
import logging

from . import consts as c
from . import utils
from .. import exceptions

from typing import Dict, Optional

class Client(object):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):

        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.first = first
        self.test = test
        self.api_url = c.API_URL
        self.proxy = None

    def _request(self, method, request_path, params, cursor=False):
        if method == c.GET:
            request_path = request_path + utils.parse_params_to_str(params)
        # url
        url = self.api_url + request_path

        # 获取本地时间
        timestamp = utils.get_timestamp()

        # sign & header
        if self.use_server_time:
            # 获取服务器时间
            timestamp = self._get_timestamp()

        if isinstance(params, str):
            body = params if method == c.POST else ""
        elif isinstance(params, dict):
            body = json.dumps(params) if method == c.POST else ""
        else:
            body = json.dumps(params) if method == c.POST else ""
        sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET_KEY)
        header = utils.get_header(self.API_KEY, sign, timestamp, self.PASSPHRASE)

        if self.test:
            header['x-simulated-trading'] = '1'
        if self.first:
            print("url:", url)
            self.first = False

        logging.debug("url: " + url)
        # print("headers:", header)
        logging.debug("body: " + body)

        # send request
        response = None
        if method == c.GET:
            if self.proxy is None:
                response = requests.get(url, headers=header)
            else:
                response = requests.get(url, headers=header, proxies=proxy)
        elif method == c.POST:
            if self.proxy is None:
                response = requests.post(url, data=body, headers=header)
            else:
                response = requests.post(url, data=body, headers=header, proxies=proxy)
        elif method == c.DELETE:
            if self.proxy is None:
                response = requests.delete(url, headers=header)
            else:
                response = requests.delete(url, headers=header, proxies=proxy)

        # exception handle
        if not str(response.status_code).startswith('2'):
            raise exceptions.OkexAPIException(response)
        try:
            res_header = response.headers
            if cursor:
                r = dict()
                try:
                    r['before'] = res_header['OK-BEFORE']
                    r['after'] = res_header['OK-AFTER']
                except:
                    pass
                return response.json(), r
            else:
                return response.json()

        except ValueError:
            raise exceptions.OkexRequestException('Invalid Response: %s' % response.text)

    def _request_without_params(self, method, request_path):
        return self._request(method, request_path, {})

    def _request_with_params(self, method, request_path, params, cursor=False):
        return self._request(method, request_path, params, cursor)

    def _get_timestamp(self):
        url = self.api_url + c.SERVER_TIMESTAMP_URL
        if self.proxy is None:
            response = requests.get(url)
        else:
            response = requests.get(url, proxies=proxy)
        if response.status_code == 200:
            return response.json()['iso']
        else:
            return ""

    def set_api_url(self, url: str):
        self.api_url = url

    def set_proxy(self, proxy: Optional[Dict]):
        self.proxy = proxy