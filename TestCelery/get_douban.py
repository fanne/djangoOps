# /usr/bin/python
#coding:utf-8

__Date__ = "2016-12-07 14:05"
__Author__ = 'eyu Fanne'



import sys
import os
import time
import urllib
import urllib2

header = {'referer':'https://www.douban.com/',
          'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
data = None

def getphoto(data):
    save_getphoto = 'G:\getphoto.txt'
    if not os.path.exists(save_getphoto):
        f = file(save_getphoto,'wb')
        try:
            f.write(data)
        finally:
            f.close()


if __name__ == "__main__":
    url = 'https://www.douban.com/'
    html = urllib2.Request(url)
    print html
    webpage = urllib2.urlopen(html)
    data = webpage.read()
    getphoto(data)





