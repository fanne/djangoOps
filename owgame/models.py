#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class owgameserver(models.Model):
    serverid = models.IntegerField(u"游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"游戏服IP")
    servername = models.CharField(u"游戏服名称",max_length=32)
    serverport = models.IntegerField(u"游戏服端口号")
    addstatus = models.IntegerField(u"开服状态",default=0) ##0:表示未在生产环境添加新服，1：代表已在生产环境添加新服

    def __unicode__(self):
        return self.servername


##海外游戏服正式服
class hw_formal_owgame(models.Model):
    serverid = models.IntegerField(u"海外正式服_游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"海外正式服_游戏服IP")
    servername = models.CharField(u"海外正式服_游戏服服名称",max_length=16)
    serverport = models.IntegerField(u"海外正式服_游戏服端口号")
    addstatus = models.IntegerField(u"开服状态",default=0) ##0:表示未在生产环境添加新服，1：代表已在生产环境添加新服

    def __unicode__(self):
        return self.servername

##海外游戏服测试服
class hw_test_owgame(models.Model):
    serverid = models.IntegerField(u"海外测试服_游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"海外测试服_游戏服IP")
    servername = models.CharField(u"海外测试服_游戏服服名称",max_length=16)
    serverport = models.IntegerField(u"海外测试服_游戏服端口号")

    def __unicode__(self):
        return self.servername



##海外游戏服审核服
class hw_audit_owgame(models.Model):
    serverid = models.IntegerField(u"海外审核服_游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"海外审核服_游戏服IP")
    servername = models.CharField(u"海外审核服_游戏服服名称",max_length=16)
    serverport = models.IntegerField(u"海外审核服_游戏服端口号")

    def __unicode__(self):
        return self.servername


##海外充值服正式服
class hw_formal_owcharge(models.Model):
    pass


##海外充值服测试服
class hw_test_owcharge(models.Model):
    pass




##海外跨服正式服
class hw_formal_owcross(models.Model):
    pass



class gn_test_owgameserver(models.Model):
    serverid = models.IntegerField(u"游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"游戏服IP")
    servername = models.CharField(u"游戏服名称",max_length=16)
    serverport = models.IntegerField(u"游戏服端口号")

    def __unicode__(self):
        return self.servername


##海外礼包序列服
class hw_owgift(models.Model):
    pass


##国内游戏服测试服
class gn_test_owgame(models.Model):
    serverid = models.IntegerField(u"国内测试服_游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"国内测试服_游戏服IP")
    servername = models.CharField(u"国内测试服_游戏服服名称",max_length=16)
    serverport = models.IntegerField(u"国内测试服_游戏服端口号")

    def __unicode__(self):
        return self.servername

##国内审核服
class gn_audit_owgame(models.Model):
    serverid = models.IntegerField(u"国内审核服_游戏服ID号",primary_key=True)
    serverhost = models.GenericIPAddressField(u"国内审核服_游戏服IP")
    servername = models.CharField(u"国内审核服_游戏服服名称",max_length=16)
    serverport = models.IntegerField(u"国内审核服_游戏服端口号")

    def __unicode__(self):
        return self.servername



