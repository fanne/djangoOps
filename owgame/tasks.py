#coding:utf-8
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from subprocess import PIPE,Popen,STDOUT
from time import sleep
from eyuOps import celery_app
import logging,os
from django.conf import settings
from owgame.models import hw_formal_owgame
from django.contrib import messages

task_logger = logging.getLogger('owgame.tasks')
ansible_owgameserver_file = os.path.join(getattr(settings,'OWGAME_ANSIBLE_HOST_DIR'),'hw_formal_owgamehost')
ansible_cmd = r'/bin/proxychains /usr/local/python27/bin/ansible --inventory-file=%s' %ansible_owgameserver_file
addServer_sh = r'/data/owserver/ow_op/tools/addserver.sh'
startServer_sh = r'/data/owinit/owServer'

# print ansible_owgameserver_file
# print ansible_cmd

@celery_app.task
def pingTest(n):
    p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
              '%s ow%s -m shell -a "ping 108.168.242.108 -c 5"' %(ansible_cmd,n),
              stdout=PIPE,stderr=STDOUT,shell=True)
    for task_log in p.stdout.readlines():
        print task_log
        task_logger.info(task_log.strip())

@celery_app.task
def NewServer(server_id):
    if hw_formal_owgame.objects.filter(pk=server_id).exists() and hw_formal_owgame.objects.filter(pk=server_id,addstatus=0):
        task_logger.info(u'开服操作,对线上服务器添加%s服' %server_id)
        dbsql = hw_formal_owgame.objects.filter(pk=server_id)
        dbport = dbsql[0].serverport
        print server_id,dbport

        ##添加新服
        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '%s ow%s -m shell -a "%s ow %s %s"' %(ansible_cmd,server_id,addServer_sh,server_id,dbport),
              stdout=PIPE,stderr=STDOUT,shell=True)
        for task_log in p.stdout.readlines():
            print task_log
            task_logger.info(task_log)

        ##启动新服
        p = Popen('source /root/.keychain/CentOS6x64-Int-sh;'
                  '%s ow%s -m shell -a "%s %s start"' %(ansible_cmd,server_id,startServer_sh,dbport),
                  stdout=PIPE,stderr=STDOUT,shell=True)
        for task_log in p.stdout.readlines():
            print task_log
            task_logger.info(task_log)

        ##更新addstatus状态
        hw_formal_owgame.objects.filter(pk=server_id).update(addstatus=1)
        # add_message = u'%s服添加成功.' %server_id
        # return add_message

    else:
        task_logger.info(u'%s服不存在服列表中,请先添加服到服列表中.' %server_id)
        # messages.add_message(request,messages.INFO, u'服列表未存在此服，请先添加.')
        # add_message = u'%s服不存在服列表中,请先添加服到服列表中.' %server_id
        # return add_message











