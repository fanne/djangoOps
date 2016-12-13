# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-14 16:47"
__Author__ = 'eyu Fanne'

###操作ansible hosts文件，在添加服和删除服时，同时操作这个文件里的记录


from models import hw_formal_owgame
from django.dispatch import receiver,Signal
from django.db.models.signals import post_delete,post_save,pre_save,pre_delete
from django.conf import settings
import os,re
import logging

ansible_hw_formal_owgame_file = os.path.join(getattr(settings,'OWGAME_ANSIBLE_HOST_DIR'),'hw_formal_owgamehost')
logger = logging.getLogger('owgame.owgame_ansible_host')

@receiver(post_save,sender=hw_formal_owgame)
def save_ansible_host(sender,instance,**kwargs):
    addserver = hw_formal_owgame.objects.filter(pk=instance.serverid)
    logger.debug(u'添加新服:服id:%s--服ip:%s--服名称:%s--服端口:%s' \
          %(addserver[0].serverid,addserver[0].serverhost,addserver[0].servername,addserver[0].serverport))
    ansiblefile = open(ansible_hw_formal_owgame_file,'a')
    ansiblefile.write('ow%s ansible_ssh_host=%s server_port=%s server_id=%s \n'
                      %(addserver[0].serverid,addserver[0].serverhost,addserver[0].serverport,addserver[0].serverid))
    ansiblefile.close()
    logger.debug(u'添加新服完成，并保存新记录到ansible hosts文件中.')


@receiver(pre_delete,sender=hw_formal_owgame)
def del_ansible_host(sender,instance,**kwargs):
    delserver = hw_formal_owgame.objects.filter(pk=instance.serverid)
    logger.debug(u'删除服:服id:%s--服ip:%s--服名称:%s--服端口:%s' \
          %(delserver[0].serverid,delserver[0].serverhost,delserver[0].servername,delserver[0].serverport))
    comment = re.compile(r'ow%s.*%s' %(delserver[0].serverid,delserver[0].serverid))
    with open(ansible_hw_formal_owgame_file,'rt') as f:
        data = f.read()

    re_data = comment.sub("",data)
    f_new = open('%s_new' %ansible_hw_formal_owgame_file,'wt')
    f_new.write(re_data)
    f_new.close()
    os.remove(ansible_hw_formal_owgame_file)
    os.rename('%s_new' %ansible_hw_formal_owgame_file,ansible_hw_formal_owgame_file)

    f = open(ansible_hw_formal_owgame_file,'a+')
    fnew = open('%s_new' %ansible_hw_formal_owgame_file,'wb')
    for line in f.readlines():
        data = line.strip()
        if len(data) != 0:
            fnew.write(data)
            fnew.write('\n')
    f.close()
    fnew.close()
    os.remove(ansible_hw_formal_owgame_file)
    os.rename('%s_new' %ansible_hw_formal_owgame_file,ansible_hw_formal_owgame_file)

    logger.debug(u'删除服完成，并把此服从ansible hosts文件中删除.')
