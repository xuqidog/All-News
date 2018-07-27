# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2018/1/29 下午3:36'
# http://www.svinsight.com/article/2.html
# 硅谷密探

from bs4 import BeautifulSoup
import requests
import os,django
import urllib2
from threading import Timer
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contacts.settings")
django.setup()
from technologyNews.models import svinsight


class script(object):
    def __init__(self):
        self.page = 1
        self.save_count = 0
        # t = Timer(1*60*60, self.write_data)  # 24*60*60 每隔一天执行一次
        # t.start()
        self.write_data()

    def write_data(self):
        html = requests.get('http://www.svinsight.com/article/2.html').content
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        list_data = soup.find('div', attrs={'class': 'col-md-9 wleft'}).find_all('div',
                                                                                 attrs={'class': 'row underline'})

        for tag in list_data:
            title = tag.find('div', attrs={'class': 'content2'}).find('h2').get_text().strip()
            summary = tag.find('div', attrs={'class': 'content2'}).find('p',
                                                                        attrs={'class': 'abstract'}).get_text().strip()
            tags = tag.find('div', attrs={'class': 'content2'}).find('p',
                                                                      attrs={'class': 'time tag2'}).get_text().strip()
            image_url = str(tag.find('p', attrs={'class': 'image'}))
            image_url = image_url[image_url.find('(') + 1:image_url.find(')')]
            url = tag.find('a').get('href')

            item = svinsight.objects.filter(url=url)
            if item:
                print (url + '已存在')
            else:
                svinsight.objects.get_or_create(
                    title='{}'.format(title),
                    summary='{}'.format(summary),
                    tags='{}'.format(tags),
                    cover='{}'.format(image_url),
                    url='{}'.format(url),
                    add_time='{}'.format(datetime.datetime.now())
                )[0]
                print (title + '添加成功')



        # listData = resp["data"]["items"]
        # self.save_count = 0
        # for one in listData:
        #     article = kr.objects.filter(id=one['id'])
        #     if article:
        #         print (str(one['id']) + '已存在')
        #     else:
        #         kr.objects.get_or_create(
        #             title='{}'.format(unicode(one['title'])),
        #             summary='{}'.format(one['summary']),
        #             extraction_tags='{}'.format(one['extraction_tags']),
        #             column_name='{}'.format(one['column_name']),
        #             cover='{}'.format(one['cover']),
        #             published_at='{}'.format(one['published_at']),
        #             id='{}'.format(one['id']),
        #         )[0]
        #         self.save_count = self.save_count + 1
        #         print (str(one['id']) + '添加成功')
        # if self.save_count == len(listData):
        #     self.page = self.page + 1
        #     print ('page' + str(self.page) + '开始添加')
        #     self.write_data()
        # else:
        #     self.page = 1
        #
        # t = Timer(1*60*60, self.write_data)  # 24*60*60 每隔一天执行一次
        # t.start()


if __name__ == '__main__':
    get = script()