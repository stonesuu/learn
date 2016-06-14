import MySQLdb as mysql

class DB():
    def __init__(self,db,host,user,passwd):
        self.db = db
        self.host = host
        self.user = user
        self.passwd = passwd
    def conn(self):
        try:
            self.conn = mysql.connect(db=self.db,host=self.host,user=self.user,passwd=self.passwd)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print 'conn err',e
        else:
            print 'conn success'
    def desc(self,table_name,table_schema=None):
        if table_schema is None:
            table_schema = self.db
        table_desc = []
        table_name = table_name
        table_schema = table_schema
        sql = '''select column_name,column_type,is_nullable,column_key,column_default,
extra from information_schema.columns where table_name="%s" and table_schema="%s"''' % (table_name,table_schema)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print 'program operation error',e
        else:
            res = self.cursor.fetchall()
            if len(res) == 0:
                print 'table not exists'
            else:
                laststr = ''
                laststr += ('|'+'Name'.center(15,'+')+'|'+'Type'.center(15,'+')+'|'+'Null'.center(5,'+')+'|'+\
                           'key'.center(5,'+')+'|'+'Default'.center(20,'+')+'|'+'Extra'.center(20,'+')+'|\n')
                for item in res:
                    #table_desc.append({'Name':item[0],'Type':item[1],'Null':item[2],'Key':item[3],'Defalut':item[4],'Extra':item[5]})
                    laststr += ('|'+str(item[0]).center(15)+'|'+str(item[1]).center(15)+'|'+str(item[2]).center(5)+'|'+str(item[3]).center(5)+\
                                '|'+str(item[4]).center(20)+'|'+str(item[5]).center(20)+'|\n')
                print laststr
    def select(self,table_name,*args,**kargs):
        argstr = ''
        if len(args)==0:
            argstr = '*,'
        else:
            for arg in args:
                argstr += arg+','
        kargstr = 'where '
        for key,val in kargs.items():
            kargstr += '%s="%s"'%(key,val)+' and '
        #print argstr
        #print kargstr
        if len(kargstr) <= 6:
            sql = 'select '+argstr[:len(argstr)-1]+' from %s'%(table_name,)
        else:
            sql = 'select '+argstr[:len(argstr)-1]+' from %s '%(table_name,)+kargstr[:len(kargstr)-5]
        print sql
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print 'select error ',e
        else:
            res = self.cursor.fetchall()
            if len(res) == 0:
                print 'no item seleted'
            else:
                print 'select success'
                self.select_result = res
    def insert(self,table_name,arg_dict):
        argstr = ''
        valuestr = ''
        for item,value in arg_dict.items():
            argstr += item+','
            valuestr += '"%s"' %(value) +','
        #print argstr
        #print valuestr
        sql = 'insert into %s(%s) values(%s)' %(table_name,argstr[:len(argstr)-1],valuestr[:len(valuestr)-1])
        #print sql
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print 'insert error ',e
        else:
            self.cursor.execute('commit')
            print 'insert success'
    def oper(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print 'opererr',e
        else:
            self.cursor.execute('commit')
            print 'oper success'
            


if __name__ == '__main__':
    db = DB('gaolei','localhost','root','123456')
    db.conn()
    sta = {}
    sta_change = {}
    #sta_list = []
    with open('D:\Python27\log.log') as f:
        for line in f:
            tmp = line.split(' ')
            key = (tmp[0],tmp[8])
            sta[key] = sta.get(key,0)+1
    #for key,count in sta.items():
        #sta_list.append((key,count))
    #for line in sorted(sta_list,key=(lambda x:x[1]),reverse=True)[:300]:
        #sql = 'insert into url_sta (ip,status,count) values ("%s",%d,%d)' % (line[0][0],int(line[0][1]),line[1])
        #db.oper(sql)
    for key,val in sta.items():
        tmp_dict = {'ip':key[0],'status':key[1],'count':val}
        db.insert('url_sta',tmp_dict)
    sql = 'commit'
    db.oper(sql)
    #sql = 'select * from url_sta'
    #print db.oper(sql)
    
    
                      
    

    
