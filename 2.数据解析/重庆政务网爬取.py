#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import etree

# 需求：爬取58二手房中的房源信息
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # 爬取到页面源码数据
    url = 'http://www.cq.gov.cn/ywdt/jrzq/'
    page_text = requests.get(url=url, headers=headers).text
    print(page_text)
    # 数据解析
    tree = etree.HTML(page_text)
    # 1.获取总页数
    total_page = tree.xpath('//*[@id="page"]/span[1]')
    print(total_page)

    # 2.进入for循环，访问地址
    # 3.统计字数，判断是否存在关键字
    # 4.输出结果





    # # 存储的就是li标签对象
    # # li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    # div_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
    # fp = open('58.txt', 'w', encoding='utf-8')
    # for div in div_list:
    #     # 局部解析
    #     title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
    #     print(title)
    #     fp.write(title + '\n')
