# /usr/bin/python
#coding:utf-8

__Date__ = "2016-12-09 10:39"
__Author__ = 'eyu Fanne'

from flask import Flask,request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("my01.html")
    # return 'Hello World!'

@app.route('/posttest',methods=["GET", "POST"])
def postTest():
    name = request.form.get("name")
    age = request.form.get("age")
    print name,age
    return render_template("postTest.html")

@app.route('/test01',methods=["GET","POST"])
def test01():
    return render_template("test01.html")


@app.route('/test02',methods=["GET","POST"])
def test02():
    return render_template("test02.html")

if __name__ == '__main__':
    app.run(debug=True)