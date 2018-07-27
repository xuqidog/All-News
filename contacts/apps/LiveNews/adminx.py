# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2018/1/26 下午1:33'

import xadmin

from .models import WangYi, TengXun


# 网易
class WangYiAdmin(object):
    list_display = ['title', 'platform', 'type', 'time']
    search_fields = ['title', 'type', 'time']
    list_filter = ['title', 'platform', 'type', 'time']
    show_bookmarks = False
    refresh_times = (3, 5)
    list_editable = ['title', 'platform']
    show_detail_fields = ['title']
    model_icon = 'fa fa-desktop'
    style_fields = {"title": "ueditor"}
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # 导入excel后数据处理逻辑
            pass
        return super(WangYiAdmin, self).post(request, args, kwargs)


# 腾讯
class TengXunAdmin(object):
    list_display = ['title', 'platform', 'type', 'time']
    search_fields = ['title', 'type', 'time']
    list_filter = ['title', 'platform', 'type', 'time']
    show_bookmarks = False
    refresh_times = (3, 5)
    list_editable = ['title', 'platform']
    show_detail_fields = ['title']
    model_icon = 'fa fa-desktop'
    style_fields = {"title": "ueditor"}
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # 导入excel后数据处理逻辑
            pass
        return super(TengXunAdmin, self).post(request, args, kwargs)


xadmin.site.register(WangYi, WangYiAdmin)
xadmin.site.register(TengXun, TengXunAdmin)