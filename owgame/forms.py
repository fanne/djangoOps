# /usr/bin/python
#coding:utf-8

__Date__ = "2016-11-18 11:30"
__Author__ = 'eyu Fanne'

from django import forms

class SqlQueryForm(forms.Form):
    SqlCmd = forms.CharField(label='SqlQuery',max_length=100)


class AddServerForm(forms.Form):
    AddNum = forms.IntegerField(label='AddServer')

class VersionForm(forms.Form):
    version = forms.IntegerField(label="Version Num")