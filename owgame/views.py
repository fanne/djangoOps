#coding:utf-8
from __future__ import absolute_import, unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

# from models import hw_formal_owgame
from owgame.models import hw_formal_owgame
from owgame.forms import SqlQueryForm,AddServerForm
from owgame.sqlquery import runSql
from owgame.tasks import pingTest,NewServer

import collections


# Create your views here.

def base(request):
    return render_to_response('base.html')


def index(request):
    return render_to_response('owindex.html')

    # return HttpResponse("The index Page")


def Hw_Formal_Owgame_SqlQuery(request):
    owdbList = hw_formal_owgame.objects.all()
    if request.method == 'POST':
        form = SqlQueryForm(request.POST)
        if form.is_valid():
            serverlist = request.POST.getlist("dbcheckbox")
            request.session['SqlCmd'] = form.cleaned_data['SqlCmd']
            if serverlist == []:
                messages.add_message(request, messages.INFO, u'未勾选游戏服')
                return redirect('owgame.views.Hw_Formal_Owgame_SqlQuery')
            else:

                request.session['indexsql'] = {}
                for server_i in serverlist:
                    dbsql = hw_formal_owgame.objects.filter(pk=server_i)
                    dbhost = dbsql[0].serverhost
                    request.session['dbname'] = dbsql[0].servername
                    request.session['sqlres']=runSql(dbhost,server_i,request.session['SqlCmd'])
                    request.session['indexsql'][server_i] = request.session['sqlres']
                messages.add_message(request, messages.INFO, u'数据库查询完成')
                request.session['sqldic'] = collections.OrderedDict(sorted(request.session['indexsql'].items(), key=lambda x: x[0]))
            return redirect('owgame.views.Hw_Formal_Owgame_SqlQuery')
    else:
        form = SqlQueryForm()
    return render(request,'Hw_Formal_Owgame_SqlQuery.html',
                  {
                      'owdbList':owdbList,
                      'form':form,
                      'SqlCmd':request.session.get('SqlCmd'),
                      'sqldic':request.session.get('sqldic'),
                      'dbname':request.session.get('dbname'),
                  }
    )




def HW_Cross_sqlQuery(request):
    return render_to_response('HW_Cross_sqlQuery.html')

def HW_Server_Test_sqlQuery(request):
    return render_to_response('HW_Server_Test_sqlQuery.html')

def GN_Server_Test_sqlQuery(request):
    return render_to_response('GN_Server_Test_sqlQuery.html')




def updateVersion(request):
    return HttpResponse('This is version updating Page')

def patch(request):
    return HttpResponse('This is patch Page')


def initServer(request):
    return render_to_response('initServer.html')


def addServer(request):
    if request.method == "POST":
        addserverfrom = AddServerForm(request.POST)
        if addserverfrom.is_valid():
            serverid = addserverfrom.cleaned_data['AddNum']
            # pingTest.delay(serverid)
            NewServer.delay(serverid)
            ##异步添加新服
            # NewServer.apply_async(request,serverid)

        return redirect('owgame.views.addServer')

    else:
        addserverfrom = AddServerForm()

    return render(request,'addServer.html',
        {
              "addserverfrom":addserverfrom,
        }
    )