# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-30 14:26"
__Author__ = 'eyu Fanne'

import requests
import time

def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print resp.status_code
    print 'use time',time.time()-start,"seconds."

if __name__ == '__main__':
    func(["http://www.sina.com.cn/","http://www.sohu.com/","http://www.ifeng.com/","http://www.qq.com/",
          "http://www.163.com/","http://docs.celeryproject.org/","http://agiliq.com/"])