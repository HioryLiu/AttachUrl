# -*- coding: utf-8 -*-
import re
from Atturl import *
import time
import MySQLdb
import json

# 查询写入测试，更新内容中附件url
t1=time.time()
cnx=MySQLdb.connect("127.0.0.1", "root",
                            "sjtuld0218","science",charset="utf8")
n=0
listn=[]
m=500
x=5800000
y=5800999
my_range=(y-x)/m+1
for i in range(my_range):

    cousor=cnx.cursor()
    sql_sentense="select * from url_content where place>=%s and place <%s"  # place为id
    sql_stentese2="update url_content set flag1=3, attach_url=%s,content=%s where place =%s"
    #atturl为附件url所在的新字段，content为内容字段
    cousor.execute(sql_sentense,(x,x+m))
    str=''
    list1=[]
    for content in cousor.fetchall():
        atturl_list=[]
        all_couple=[]
        str1=content[3]
        con_url=content[2]
        con_id=content[0]

        str2=Replace_Char(str1)
        pre_url=get_url(str2)
        for i in pre_url:
            a=combin_url(get_domain(con_url,has_http(i)),i)
            atturl_list.append(a)
            all_couple.append((i,a))

        for i in all_couple:
            str2=str2.replace(i[0],i[1])

        if atturl_list:
            print [atturl_list,con_id]
            encodedjson = json.dumps(atturl_list)
            list1.append((encodedjson,str2,con_id))


    tuple_in=tuple(list1)
    cousor.close()
    cursor2=cnx.cursor()
    cursor2.executemany(sql_stentese2,tuple_in)
    cnx.commit()
    cursor2.close()

    x=x+m
    print x



    t2=time.time()
    print t2-t1
cnx.close()
t3=time.time()
print t3-t1
