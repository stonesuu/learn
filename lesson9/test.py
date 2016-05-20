#-*- coding:utf-8 -*-
from flask import Flask,request,render_template,json
import logoper as log

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('tableshow.html')

@app.route('/tableget')
def tableget():
    sql = 'select * from test'
    try:
        log.sqloper(sql)
    except:
        print 'error'
        return 'error'
    else:
        #print log.cursor.fetchall()#如果这个执行了一次
        res = json.dumps(log.cursor.fetchall())#那这一次执行就是空值
        #print res
        return res

@app.route('/adduser')
def adduser():
    user = request.args.get('username')
    passwd = request.args.get('password')
    sql = 'insert into test(username,password) values("%s","%s")' % (user,passwd)
    try:
        log.sqloper(sql)
        log.sqloper('commit')
    except:
        return 'error'
    else:
        return 'ok'



@app.route('/deluser')
def deluser():
    del_id = request.args.get('id')
    sql = 'delete from test where id=%s' % del_id
    try:
        log.sqloper(sql)
        log.sqloper('commit')
    except:
        return 'error'
    else:
        return 'ok'






if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9023,debug=True)
