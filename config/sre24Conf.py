import sys
import traceback

import requests

import TickerConfig


def sendSre24Push(msg: str, token: str = TickerConfig.SRE24_TOKEN, prefix: str = '[12306]'):
    try:
        if not token:
            return
        msg = prefix + msg
        rs = requests.post(url="https://push.jwks123.com/api/v1/push", json=dict(token=token, msg=msg), timeout=5).json()
        assert int(rs["code"] / 100) == 2, rs
    except:
        traceback.print_exc(file=sys.stderr)


if __name__ == '__main__':
    sendSre24Push(msg="1")
