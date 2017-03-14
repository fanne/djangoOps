# /usr/bin/python
#coding:utf-8

__Date__ = "2016-12-16 16:28"
__Author__ = 'eyu Fanne'

#-*-coding:utf-8-*-

from Tkinter import *
import tkMessageBox
import csv
import random
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

global jdyx,root,ksms,score
qb = 0
q_num = []
choose = [] #存储选项
right_c = [] #存储每道题的答案
your_c = [] #自己选择的答案
content = [] #用来读取题目的存储



def open_QuestionBank():
    with open("150ti.csv") as csvfile: #打开csv文件
        reader = csv.reader(csvfile)
        p = []
        for row in reader:
          nrow = []
          for r in row:
            nrow.append(r.decode('utf-8'))
          p.append(nrow)
    return p

"反馈信息界面"
def fkxx():
    tkMessageBox.showinfo( "反馈信息", "邮箱：xxx@163.com")

"答题得分界面"
def defen():
    ksms.destroy()
    df = Tk()
    df.title('考试结果')
    df.geometry('200x80')

    Label(df,text = '你的得分为：').pack()
    Label(df,text = str(score)).pack()

def get_question():

    while 1:
        tnum = random.randint(0,len(qb) -1)
        if tnum in q_num:
            pass
        else:
            q_num.append(tnum)
            break
    "获取用户的选择，存在your_c中"
    your_c.append(choose[0].get())

    "设置题干"
    cont = '    %s、'%len(q_num)
    cont += qb[tnum][0]
    content[0].set(cont)
    "做完25道题"
    if content[6].get() == '提交':
        global score
        score = sum(list(map(lambda x: x[0]==x[1], zip(right_c, your_c))) )*4
        defen()
        print(score)

    if len(q_num) == 25:
        content[6].set('提交')


    "设置选项"
    for i in range(1,5):
        content[i].set(qb[tnum][i])

    "找出正确答案，存在list right_c中"
    rs = re.findall('\w',qb[tnum][5])
    if len(rs):
        right_c.append(rs[0])
    else:
        right_c.append('0')
        #print '题目有问题，文件中无答案'


    choose[0].set('0')


def ksms():
    "考试模式界面"
    jdyx.destroy()
    global ksms
    ksms = Tk()
    ksms.title('考试')

    ksms.geometry('600x400')
    "创建Label用于显示题干"
    for i in range(7):
        content.append(StringVar())

    content[6].set('下一题')
    choose.append(StringVar())
    choose[0].set(0)
    get_question()
    Label(ksms, textvariable = content[0],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left').pack()#题干

    "选项"
    rb = Radiobutton(ksms,variable=choose[0],value='A',textvariable=content[1],width = 300,height = 3,wraplength = 300,anchor = 'e',justify = 'left')
    rb.place(x = 30, y = 50)
    rb = Radiobutton(ksms,variable=choose[0],value='B',textvariable=content[2],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    rb.place(x = 30, y = 100)
    rb = Radiobutton(ksms,variable=choose[0],value='C',textvariable=content[3],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    rb.place(x = 30, y = 150)
    rb = Radiobutton(ksms,variable=choose[0],value='D',textvariable=content[4],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    rb.place(x = 30, y = 200)

    Button(ksms,textvariable = content[6], command = get_question).place(x = 300, y = 260)

    ksms.mainloop()


def tj_q():
    "判断该题是否做对"

    rs = re.findall('\w',qb[q_num[-1]][5])
    if len(rs):
        r = (rs[0])
    else:
        r = '0'
       #print '题目有问题，文件中无答案'
    if choose[0].get() == r:
        content[7].set('你的答案正确')
    else:
        content[7].set('你的答案错误，正确的选项是%s'%r)

def get_q():
    "按顺序获取题目"
    tnum = len(q_num)
    q_num.append(tnum)
    "设置题干"
    cont = '    %s、'%(tnum+1)
    cont += qb[tnum][0]
    content[0].set(cont)

    if len(q_num) == 150:
        content[6].set('null')
        content[7].set('没有题目了')

    "设置选项"
    for i in range(1,5):
        content[i].set(qb[tnum][i])

    content[7].set('   ')
    choose[0].set('0')

def zydt():
    "自由模式界面"
    jdyx.destroy()
    zydt = Tk()
    zydt.title('考试')

    zydt.geometry('600x400')
    "创建Label用于显示题干"
    for i in range(8):
        content.append(StringVar())

    content[6].set('下一题')
    content[7].set('  ')
    choose.append(StringVar())
    choose[0].set(0)
    get_q()
    Label(zydt, textvariable = content[0],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left').pack()#题干

    "选项"
    rb = Radiobutton(zydt,variable=choose[0],value='A',textvariable=content[1],width = 300,height = 3,wraplength = 300,anchor = 'e',justify = 'left')
    rb.place(x = 30, y = 50)
    rb = Radiobutton(zydt,variable=choose[0],value='B',textvariable=content[2],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    rb.place(x = 30, y = 100)
    rb = Radiobutton(zydt,variable=choose[0],value='C',textvariable=content[3],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    rb.place(x = 30, y = 150)
    rb = Radiobutton(zydt,variable=choose[0],value='D',textvariable=content[4],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    rb.place(x = 30, y = 200)

    Button(zydt,text = '提交', command = tj_q).place(x = 200, y = 260)
    Button(zydt,text = '下一题', command = get_q).place(x = 300, y = 260)
    lb = Label(zydt, textvariable = content[7],width = 600,height = 3,wraplength = 600,anchor = 'w',justify = 'left')
    lb.place(x = 30, y = 300)
    zydt.mainloop()


def jdyx():
    '''竞答游戏界面'''
    global jdyx
    root.destroy()
    jdyx = Tk()
    jdyx.title('竞答游戏')
    canvas = Canvas(jdyx,width = 600, height = 400, bg = 'blue')
    canvas.pack(expand = YES, fill = BOTH)
    btn = Button(jdyx, text ='自由答题',command = zydt, bg ='#ffffff')
    btn.place(x = 270, y = 100)
    btn1 = Button(jdyx, text ='考试模式',command = ksms, bg ='#ffffff')
    btn1.place(x = 270, y = 200)
    btn2 = Button(jdyx, text ='反馈信息',command = fkxx, bg ='#ffffff')
    btn2.place(x = 270, y = 300)
    jdyx.mainloop()

def ui():
    '''欢迎界面'''
    global root
    root = Tk()
    root.title('开始界面')
    canvas = Canvas(root,width = 600, height = 400, bg = 'blue')
    canvas.pack(expand = YES, fill = BOTH)

    btn1 = Button(root, text ='竞答游戏',command = jdyx, bg ='blue')
    btn1.place(x = 270, y = 220)
    root.mainloop()



if __name__ == "__main__":
    qb = open_QuestionBank()
    ui()
