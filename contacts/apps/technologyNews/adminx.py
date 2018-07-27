# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2018/1/26 下午4:51'

import xadmin

from .models import kr, svinsight


# 36kr
class krAdmin(object):
    list_display = ['title', 'column_name', 'published_at', 'id']
    search_fields = ['id', 'title', 'column_name', 'published_at']
    list_filter = ['id', 'title', 'column_name', 'published_at']
    show_bookmarks = False
    refresh_times = (3, 5)
    # list_editable = ['title', 'column_name']
    show_detail_fields = ['title']
    model_icon = 'fa fa-globe'
    style_fields = {"title": "ueditor"}
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # 导入excel后数据处理逻辑
            pass
        return super(krAdmin, self).post(request, args, kwargs)


# 硅谷密探
class svinsightAdmin(object):
    list_display = ['title', 'tags', 'add_time']
    search_fields = ['title', 'tags', 'add_time']
    list_filter = ['title', 'tags', 'add_time']
    show_bookmarks = False
    refresh_times = (3, 5)
    # list_editable = ['title', 'column_name']
    show_detail_fields = ['title']
    model_icon = 'fa fa-globe'
    style_fields = {"title": "ueditor"}
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # 导入excel后数据处理逻辑
            pass
        return super(svinsightAdmin, self).post(request, args, kwargs)


xadmin.site.register(kr, krAdmin)
xadmin.site.register(svinsight, svinsightAdmin)