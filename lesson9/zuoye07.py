#-*- coding: utf-8 -*-
import logoper as log
from flask import Flask,render_template,request,redirect,session,json
app = Flask(__name__)
app.secret_key = 'sadfagraegrgaregareghhqare'
page = 1 #页数

@app.route('/testdata')
def testdata():
    return 'hello ajax'

@app.route('/tableshow')
def tableshow():
    sql = 'select * from user'
    log.sqloper(sql)
    return render_template('tableshow.html',datalist=log.cursor.fetchall())
    #return 'test'

@app.route('/gettable_old')
def gettable_old():
    sql= 'select * from user'
    res = ''
    log.sqloper(sql)
    for line in log.cursor.fetchall():
        res += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % line
    return res

@app.route('/gettable')
def gettable():
    sql = 'select * from user'
    log.sqloper(sql)
    res = json.dumps(log.cursor.fetchall())
    return res

@app.route('/adduser')
def adduser():
    username = request.args.get('user')
    password = request.args.get('passwd')
    sql = 'insert into user (username,password) values ("%s","%s")' % (username,password)
    try:
        log.sqloper(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/deluser')
def deluser():
    id = request.args.get('id')
    sql = 'delete from user where id=%s' % id
    try:
        log.sqloper(sql)
    except:
        return 'error'
    else:
        return 'ok'

    

@app.route('/login',methods=['GET','POST'])
def login():
    global page
    if 'user' in session:
        page = 1
        return redirect('/%d' % page)
    else:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            namelist = []
            name = request.form.get('user')
            pwd = request.form.get('passwd')
            sql = 'select username from user'
            log.sqloper(sql)
            for line in log.cursor.fetchall():
                namelist.append(line[0])
            if name in namelist:
                sql = 'select password from user where username="%s"' % name
                log.sqloper(sql)
                if pwd == log.cursor.fetchone()[0]:
                    session['user'] = name
                    page = 1
                    return redirect('/url')
                else:
                    return render_template('login.html',result='password error')
            else:
                return render_template('login.html',result='username not exist')

@app.route('/url')
def url():
    return render_template('url_sta.html')
            

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/getsta')
def getsta():
    sql = 'select * from url_sta'
    log.sqloper(sql)
    res = json.dumps(log.cursor.fetchall())
    return res

@app.route('/<int:page>')#显示数据
def url_sta(page):
    if not 'user' in session:
        return redirect('/login')
    page = page
    if page < 1 or page > 5:
        return 'page error'
    sql = 'select id,ip,status,count from url_sta limit %d,20' % (20*(page-1))
    log.sqloper(sql)
    return render_template('url_sta.html',datalist=log.cursor.fetchall(),page=page)

@app.route('/change',methods=['post']) #选择页数的页面
def change():
    global page
    oper = request.form.get('oper')
    if oper == 'plus' and page < 5:
        page += 1
    elif oper == 'delete' and page > 1:
        page -= 1
    elif oper=='turnto':
        page = int(request.form.get('page'))
        
    return redirect('/%d' % page)

@app.route('/usermanage')
def usermanage():
    sql = 'select * from user'
    log.sqloper(sql)
    if session['user'] == 'admin':
        return render_template('user_manage.html',datalist=log.cursor.fetchall())
    else:
        return redirect('/login')
    
            
        

if __name__ == '__main__':

    app.run(host = '0.0.0.0',port = 9023,debug = True)
