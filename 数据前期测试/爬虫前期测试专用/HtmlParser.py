""" 
@author:jansonlv
@file: HtmlParser.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

# import re
from bs4 import BeautifulSoup
from lxml import etree

class HtmlParser(object):
    def parser(self, html_content):
        '''
        用于解析网页内容,抽取url和数据
        :param page_url: 下载页面的url????
        :param html_content: 下载的网页内容
        :return: 返回url和数据
        '''
        if not html_content:
            print('无网页数据')
            return
        soup = etree.HTML(html_content)

        self._get_new_urls(soup)

    def _get_new_urls(self, soup):
        '''
        抽取新的url集合
        :param page_url: 下载页面的url???
        :param html_content: html页面内容
        :return: 返回新的url集合
        '''
        result = soup.xpath("")





'''

    body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div:nth-child(1) > a
    body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div:nth-child(2) > a:nth-child(1)
    body > div.body - wrapper > div.content - wrapper > div > div.main - content > div.lemma - summary > div > a.xh - highlight
'''
