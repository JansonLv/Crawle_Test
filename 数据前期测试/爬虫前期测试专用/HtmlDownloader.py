""" 
@author:jansonlv
@file: HtmlDownloader.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

import requests
from urllib.parse import urlencode


class HtmlDownloader(object):

    def download(self, url, headers=None, get_data=None, post_data=None, filepath=None):
        '''

        :param url:
        :param data:
        :param post_data:
        :return:
        '''
        if not url:
            print('请输入url')
            return None
        # 随机获取下载头
        if not headers:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}

        # 如果post_data为0，则请求方式为get
        if not post_data and get_data:
            data_url = urlencode (get_data)
            url = url + '?' + data_url
            print('执行get--->', url)
            html = requests.get(url, headers=headers, data=get_data)
        elif post_data:
            if get_data:
                # 拼接url
                data_url = urlencode (get_data)
                url = url + '?' + data_url
            print('执行post------->', url)
            html = requests.post(url,  headers=headers, data=post_data)
        else:
            print('请求--------》', url)
            html = requests.get(url, data=get_data, headers=headers)

        if html.status_code == 200:
            print('------------------------------------------')
            html.encoding = 'utf-8'
            print('******************************************')
            print(html.content)
            print('******************************************')
            if filepath:
                with open(filepath, 'wb') as f:
                    f.write(html.content)
            return html.content
        return None

def main():
    test = HtmlDownloader()
    get_dict = {
        'wd' : '啊啊啊'
    }
    post_dict = {
        'wd': 'aaa'
    }
    test.downlooad('https://baike.baidu.com/item/%E8%9C%98%E8%9B%9B/8135707')

# 测试
if __name__ == '__main__':
    main()
