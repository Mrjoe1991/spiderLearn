# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = 'utf-8'
    page_text = page_text.text
    print(page_text)