import requests
import logoper as log
import json
ak = 'zkGu5IxVRWfTeWhlGnLQnuGR4498csyE'
url = 'http://api.map.baidu.com/location/ip'
db = log.DB('gaolei','localhost','root','123456')
db.conn()
db.select('url_sta','IP','status','count')
for item in db.select_result:
    tmp = requests.get('%s?ak=%s&ip=%s&coor=db09ll'%(url,ak,item[0]))
    res = tmp.json()
    if res['status'] == 0:
        #print res['content']['point']
        insert_dict = {}
        insert_dict['ip']=item[0]
        insert_dict['status']=item[1]
        insert_dict['count']=item[2]
        insert_dict['geox']=res['content']['point']['x']
        insert_dict['geoy']=res['content']['point']['y']
        db.insert('geosta',insert_dict)
        
    
    


