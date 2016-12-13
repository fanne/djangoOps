# /usr/bin/python
#coding:utf-8

__Date__ = "2016-10-21 11:26"
__Author__ = 'eyu Fanne'

from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.index,name='index'),

    ##数据库查询
    url(r'Hw_Formal_Owgame_SqlQuery/',views.Hw_Formal_Owgame_SqlQuery,name='Hw_Formal_Owgame_SqlQuery'),
    url(r'HW_Cross_sqlQuery/',views.HW_Cross_sqlQuery,name='HW_Cross_sqlQuery'),
    url(r'HW_Server_Test_sqlQuery/',views.HW_Server_Test_sqlQuery,name='HW_Server_Test_sqlQuery'),
    url(r'GN_Server_Test_sqlQuery/',views.GN_Server_Test_sqlQuery,name='GN_Server_Test_sqlQuery'),

    ##版本更新
    url(r'update/',views.updateVersion,name='update'),

    ##打补丁
    url(r'patch/',views.patch,name='patch'),

    ##初始化服务器
    url(r'initServer/',views.initServer,name='initServer'),

    ##添加新服
    url(r'addServer/',views.addServer,name='addServer'),
]