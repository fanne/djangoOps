# /usr/bin/python
#coding:utf-8

__Date__ = "2016-04-07 17:33"
__Author__ = 'eyu Fanne'

import logging


def logConfig(prolog,logdir):
    logger = logging.getLogger(prolog)  #设置log域
    logger.setLevel(logging.DEBUG)
    fmter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    hdlr = logging.FileHandler(logdir)  #输出到文件
    # print 'logdirlogdirlogdirlogdir%s' %logger
    console = logging.StreamHandler()   #输出到控制台
    # hdlr.setFormatter(fmter)        #文件输出格式
    # console.setFormatter(fmter)     #控制台输出格式
    logger.addHandler(hdlr)
    logger.addHandler(console)
    return logger