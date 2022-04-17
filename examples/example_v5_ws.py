
'''
Here is the okex ws api example.

'''

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
)

import json

from okex.v5.ws_api import WebSocketAPI, WebSocketClient, Channel
from okex.v5.insttype import InstType

import asyncio
import time

async def main():
    if os.path.exists('api.json'):
        config_path = 'api.json'
    elif os.path.exists('examples/api.json'):
        config_path = 'examples/api.json'
    elif os.path.exists('../api.json'):
        config_path = '../api.json'

    with open(config_path, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    api_key = obj['api_key']
    secret_key = obj['secret_key']
    passphrase = obj['passphrase']

    async with WebSocketClient(api_key, secret_key, passphrase, test=True) as api:
        await api.subscribe(Channel(name='instruments', instType=InstType.SPOT))
        # await api.subscribe(Channel(name='tickers', instId='BTC/USDT'))
        # await api.subscribe(Channel(name='account'))
        while True:
            await asyncio.sleep(0.5)
            msg = await api.recv()
            print(msg)

if __name__ == '__main__':
    asyncio.run(main())