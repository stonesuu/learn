#-*- coding: utf-8 -*-
import logoper as log
from flask import Flask,render_template,request,redirect,session,json
app = Flask(__name__)
app.secret_key = 'sadfagraegrgaregareghhqare'
page = 0

db = log.DB('gaolei','localhost','root','123456')
db.conn()
@app.route('/login',methods=['GET','POST'])
def login():
    global page
    if 'user' in session:
        return redirect('/url')
    else:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            namelist = []
            name = request.form.get('user')
            pwd = request.form.get('passwd')
            print name,pwd
            #sql = 'select username from user'
            #log.sqloper(sql)
            db.select('user','username')
            for line in db.select_result:
                print line
                namelist.append(line[0])
            if name in namelist:
                #sql = 'select password from user where username="%s"' % name
                #log.sqloper(sql)
                db.select('user','password',username='"%s"'% name)
                tmp = db.select_result
                if pwd == tmp[0][0]:
                    session['user'] = name
                    page = 0
                    return redirect('/url')
                else:
                    return render_template('login.html',result='password error')
            else:
                return render_template('login.html',result='username not exist')



            


@app.route('/url')
def url():
    if 'user' in session:
        return render_template('url_sta.html')
    else:
        return redirect('/login')

@app.route('/user')
def user():
    if 'user' in session:
        return render_template('user_manage.html')
    else:
        return redirect('/login')
            

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


@app.route('/getsta')
def getsta():
    sql = 'select * from url_sta limit %d,20' % (page*20,)
    #log.sqloper(sql)
    tmp = db.oper(sql)
    res = json.dumps(tmp)
    return res

@app.route('/getpage')
def getpage():
    global page
    oper = request.args.get('oper')
    if oper == 'plus' and page < 4:
        page += 1
        return 'ok'
    elif oper == 'delete' and page > 0:
        page -= 1
        return 'ok'
    elif oper == 'turnto':
        page = int(request.args.get('page'))
        return 'ok'
    else:
        return 'error'

@app.route('/getuser')
def getuser():
    sql = 'select * from user'
    #log.sqloper(sql)
    tmp = db.oper(sql)
    res = json.dumps(tmp)
    return res

@app.route('/adduser')
def adduser():
    if 'user' not in session:
        return redirect('/login')
    else:
        user = request.args.get('user')
        passwd = request.args.get('passwd')
        sql = 'insert into user(username,password) values("%s","%s")' % (user,passwd)
        try:
            db.oper(sql)
            db.oper('commit')
        except:
            return 'error'
        else:
            return 'ok'

@app.route('/deluser')
def deluser():
    if 'user' in session:
        return redirect('/url')
    else:
        num = request.args.get('id')
        sql = 'delete from user where id=%s' % num
        try:
            db.oper(sql)
        except:
            return 'error'
        else:
            return 'ok'

@app.route('/update')
def update():
    num = request.args.get('id')
    passwd = request.args.get('passwd')
    sql = 'update user set password="%s" where id=%s' % (passwd,num)
    try:
        db.oper(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/host')
def host():
    return render_template('host_manage.html')

@app.route('/gethost')
def gethost():
    sql = 'select * from host'
    #log.sqloper(sql)
    tmp = db.oper(sql)
    res = json.dumps(tmp)
    return res

@app.route('/addhost')
def addhost():
    host = request.args.get('host')
    mem = int(request.args.get('mem'))
    date = request.args.get('date')
    email = request.args.get('email')
    sql = 'insert into host(hostname,memory,date,email) values("%s",%s,"%s","%s")' % (host,mem,date,email)
    try:
        db.oper(sql)
        db.oper('commit')
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/updatehost')
def updatehost():
    num = request.args.get('id')
    host = request.args.get('host')
    mem = int(request.args.get('mem'))
    date = request.args.get('date')
    email = request.args.get('email')
    sql = 'update host set hostname="%s",memory=%s,date="%s",email="%s" where id=%s' % (host,mem,date,email,num)
    try:
        db.oper(sql)
        db.oper('commit')
    except:
        return 'error'
    else:
        return 'ok'
    
@app.route('/delhost')
def delhost():
    num = request.args.get('id')
    sql = 'delete from host where id=%s' % num
    try:
        db.oper(sql)
    except:
        return 'error'
    else:
        return 'ok'

@app.route('/geomap')
def geomap():
    if 'user' in session:
        return render_template('geomap.html')
    else:
        return redirect('/login')
@app.route('/getgeo')
def getgeo():
    db.select('geosta')
    return json.dumps(db.select_result)

if __name__ == '__main__':

    app.run(host = '0.0.0.0',port = 9023,debug = True)



