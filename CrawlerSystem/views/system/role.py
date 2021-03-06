#! /usr/bin/python
# -*- coding: utf-8 -*-
#
#管理员相关
#
#django 常用导入
#=========================================
from django.core.urlresolvers import reverse  
from django.db import connection,connections
from django.utils.html import conditional_escape 
from django.http import HttpResponse
from django.shortcuts import redirect,render_to_response,HttpResponseRedirect,render
from django.views.generic import ListView,View
from django.template import loader, RequestContext
#==========================================

import sys
import datetime, time
from urls.AutoUrl import Route
from settings import TITLE
from CrawlerSystem.models.admin import Admin
from CrawlerSystem.models.log import Log
from django.http import HttpResponseRedirect


@Route()
def role_list(request):
    '''角色列表
    '''
    if request.admin.is_manager:
        list_record = request.admin.get_resource('role')
    return render_to_response('system/role_list.html', locals())