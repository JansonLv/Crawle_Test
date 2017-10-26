""" 
@author:jansonlv
@file: spider.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

from DataOutput import DataDeal
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
import settings


class Spider(object):
    def __init__(self):
        self.html_parser = HtmlParser()
        self.html_downloader = HtmlDownloader()
        self.data_save = DataDeal()

    def crawl(self, start_url):
        '''
        爬虫执行程序
        :param start_url: 爬虫开始地址
        :return: 无
        '''
        # 网页下载
        headers = settings.headers
        get_data = settings.get_data
        post_data = settings.post_data
        filepath = settings.filepath
        html = self.html_downloader.download(start_url, headers=headers, get_data=get_data, post_data=post_data, filepath=filepath)

        # 解析网页


def main():
    spider = Spider()
    url = 'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F211978%2F&t=2017102621453789814&Ajax_CallBackArgument0=211978'
    spider.crawl(url)


if __name__ == '__main__':
    main()
