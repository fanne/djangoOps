# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-18 17:59"
__Author__ = 'eyu Fanne'

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})