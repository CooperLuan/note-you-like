import requests
import random

from models.base import BaseModel

USER_AGENT_LIST = [
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.2.15 Version/10.00',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; zh-cn) Opera 11.00',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.30 Version/10.61',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
]


class URLModel(BaseModel):

    def __init__(self, url, proxies=None, cookies=None):
        self.url = url
        self.proxies = proxies
        self.cookies = cookies

    def get_html(self):
        headers = {
            'User-Agent': random.choice(USER_AGENT_LIST),
        }
        resp = requests.get(
            self.url,
            headers=headers,
            cookies=self.cookies or {},
            proxies=self.proxies or {},
        )
        return resp.content.decode(resp.encoding)
