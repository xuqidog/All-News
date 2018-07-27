# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2018/1/26 上午11:34'


import xadmin
from .models import YouDao


class YouDaoAdmin(object):
    list_display = ['title', 'channelName', 'type', 'time']
    search_fields = ['title', 'type', 'time']
    list_filter = ['title', 'channelName', 'type', 'time']
    show_bookmarks = False
    refresh_times = (3, 5)
    list_editable = ['title', 'channelName']
    show_detail_fields = ['title']
    model_icon = 'fa fa-inbox'
    style_fields = {"title": "ueditor"}
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # 导入excel后数据处理逻辑
            pass
        return super(YouDaoAdmin, self).post(request, args, kwargs)


xadmin.site.register(YouDao, YouDaoAdmin)
