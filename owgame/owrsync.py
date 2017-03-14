# /usr/bin/python
#coding:utf-8

__Date__ = "2016-04-07 18:50"
__Author__ = 'eyu Fanne'


from threading import Thread
from app.common.myLogConfig import logConfig
from app.common.svnRsync import svnRsyncPro
import time,os



logdir = 'logs/'
logfile = logdir + 'owrsync_log.text'
logname = 'owlog'
mylogger = logConfig(logname,logfile)  #填入域跟路径
print logfile




def RsryncWork(app,proDic,proId,versionNum):
    stattime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    baklog = '%s.%s' %(logfile,stattime)
    os.popen('cp -rf %s %s' %(logfile,baklog))
    os.popen('echo "" > %s' %logfile)
    rsyncwork = svnRsyncPro(mylogger)   #使用logConfig引入log模块来记录日志信息
    project_name = proDic.get('%s' %proId)['pro_name']
    project_local_dir = proDic.get('%s' %proId)['pro_dir']
    project_online_dir = proDic.get('%s' %proId)['ol_dir']

    mylogger.info('===================我是华丽分割线================================')
    mylogger.info('================最新一次更新时间%s==========================='%stattime)


    with app.app_context():
        rsyncwork.get_version(project_local_dir)
        rsyncwork.online_laste(project_online_dir,project_name)
        rsyncwork.up_svn(versionNum,project_local_dir)
        rsyncwork.rsync_file(project_local_dir,project_online_dir,project_name)
        rsyncwork.add_commit(project_online_dir,project_name,versionNum)


def startRsync(app,proDic,proId,versionNum):
    thr = Thread(target=RsryncWork,args=[app,proDic,proId,versionNum])
    thr.start()
    return thr