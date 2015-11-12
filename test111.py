# -*- coding: utf-8 -*-
from mysql import connector
from attatch_url import attatch_url
import time
import json
import myjson



t1=time.time()
cnx=connector.Connect(host=myjson.host, user=myjson.username,
                            password=myjson.password, database=myjson.database, charset="utf8")
n=0
listn=[]
m=myjson.apart_num
x=myjson.range_start
y=myjson.range_end
my_range=(y-x)/m+1
for i in range(my_range):
    t6=time.time()

    cursor=cnx.cursor()
    sql_sentense="select * from url_content where place>=%s and place <%s"
    sql_sentense2='update url_content set flag1=1, attach_url=%s where place =%s'
    cursor.execute(sql_sentense,(x,x+m))
    list1=[]
    str=''
    for content in cursor.fetchall():
        # str='''<a href="/InvestmentInfo/ZhaoBiao/InviteNoticeDetail.aspx?id=127814">zhanghong4@tiens.com<'''
        str=content[3]
        # url1=content[2]
        # print url1.encode('GBK','ignore')
        att_url=content[2]
        text = attatch_url(str,att_url)
        url=text.get_attatch_url()
        con_id=content[0]
        if url != []:
            encodedjson = json.dumps(url)
            list1.append((encodedjson,con_id))
        else:
            list1.append((('',con_id)))
    # print list1
    tuple_in=tuple(list1)
    # print tuple_in
    print x
    cursor.close()
    cursor2=cnx.cursor()
    cursor2.executemany(sql_sentense2,tuple_in)
    cnx.commit()
    # print 'executemany ok'
    cursor2.close()


    t2=time.time()
    t3 =t2-t1
    t7=t2-t6
    print t3
    if t7>10:
        listn.append((x,t7))
    x=x+m
cnx.close()
t4=time.time()
t5=t4-t1
print t5
print listn