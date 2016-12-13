# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-30 15:31"
__Author__ = 'eyu Fanne'

from celery import Celery
import requests
import time

from celery import Celery

app = Celery('with_celery', broker='redis://localhost:6379/0')

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print resp.status_code

def func(urls):
    for url in urls:
        fetch_url.delay(url)

if __name__ == "__main__":
    func(["http://www.sina.com.cn/","http://www.sohu.com/","http://www.ifeng.com/","http://www.qq.com/",
          "http://www.163.com/","http://docs.celeryproject.org/","http://agiliq.com/"])
