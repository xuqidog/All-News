# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2018/1/26 下午5:07'
# 36kr文章定时获取

import os,django
import urllib2
import json
import pprint
from threading import Timer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contacts.settings")
django.setup()
from technologyNews.models import kr


class script_kr(object):
    def __init__(self):
        self.page = 1
        self.save_count = 0
        t = Timer(1*60*60, self.write_data)  # 24*60*60 每隔一天执行一次
        t.start()

    def write_data(self):
        u = urllib2.urlopen(
            'http://36kr.com/api/search-column/mainsite?per_page=4&page=' + str(self.page) + '&_=1516953429055')
        resp = json.loads(u.read().decode('utf-8'))
        listData = resp["data"]["items"]
        self.save_count = 0
        for one in listData:
            article = kr.objects.filter(id=one['id'])
            if article:
                print (str(one['id']) + '已存在')
            else:
                kr.objects.get_or_create(
                    title='{}'.format(unicode(one['title'])),
                    summary='{}'.format(one['summary']),
                    extraction_tags='{}'.format(one['extraction_tags']),
                    column_name='{}'.format(one['column_name']),
                    cover='{}'.format(one['cover']),
                    published_at='{}'.format(one['published_at']),
                    id='{}'.format(one['id']),
                )[0]
                self.save_count = self.save_count + 1
                print (str(one['id']) + '添加成功')
        if self.save_count == len(listData):
            self.page = self.page + 1
            print ('page' + str(self.page) + '开始添加')
            self.write_data()
        else:
            self.page = 1

        t = Timer(1*60*60, self.write_data)  # 24*60*60 每隔一天执行一次
        t.start()


if __name__ == '__main__':
    get = script_kr()