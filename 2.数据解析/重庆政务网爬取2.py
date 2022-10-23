#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

keywords_list = ['邓恢林', '薄熙来', '孙政才', '王立军', '薄王', '遗毒']

# 需求：爬取三国演义小说所有的章节标题和章节内容http://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == "__main__":
    # 对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    # 根据页数，直接写死
    article_num = 0
    word_num = 0
    snsitive_urls = {}
    for page in range(67):
        if page == 0:
            url = 'http://www.cq.gov.cn/ywdt/bmts/'
        else:
            url = 'http://www.cq.gov.cn/ywdt/bmts/index_{}.html'.format(page)

        # url = 'http://sousuo.gov.cn/column/19423/{}.htm'.format(page)

        page_text = requests.get(url=url, headers=headers)
        page_text.encoding = 'utf-8'
        page_text = page_text.text
        # 在首页中解析出章节的标题和详情页的url
        # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
        soup = BeautifulSoup(page_text, 'lxml')
        # 2.解析章节标题和详情页的url
        li_list = soup.select('.common-list > ul > li')
        # fp = open('./sanguo.txt', 'w', encoding='utf-8')
        for li in li_list:
            title = li.a.string
            detail_url = 'http://www.cq.gov.cn/ywdt/bmts/' + li.a['href'].split('/', 1)[1]
            # 对详情页发起请求，解析出章节内容
            # detail_page_text = requests.get(url=detail_url, headers=headers).text
            detail_page_text = requests.get(url=detail_url, headers=headers)
            detail_page_text.encoding = 'utf-8'
            detail_page_text = detail_page_text.text
            # 解析出详情页中相关的章节内容
            detail_soup = BeautifulSoup(detail_page_text, 'lxml')
            div_tag = detail_soup.find('div', class_='c-txt')
            # 解析到了章节的内容
            content = div_tag.get_text()
            print(content)
            for keyword in keywords_list:
                if keyword in content or keyword in title:
                    if detail_url in snsitive_urls:
                        # print(snsitive_urls[detail_url], type(snsitive_urls[detail_url]), keyword, type(keyword))
                        snsitive_urls[detail_url].append(keyword)
                    else:
                        snsitive_urls[detail_url] = [keyword]
                    # print(detail_url, keyword)
            # print('第{}结束'.format(article_num))
            # print(snsitive_urls)
            article_num += 1
            word_num += len(content)
            # fp.write(title + ':' + content + '\n')
    for k, v in snsitive_urls.items():
        print(k, v)
    print(article_num)
    print(word_num)









