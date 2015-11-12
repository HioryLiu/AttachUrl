# -*- coding: utf-8 -*-
import re
from attatch_url import attatch_url
import time
import MySQLdb

# 单条信息测试，未写入。
t1=time.time()
cnx=MySQLdb.connect("127.0.0.1", "root",
                            "sjtuld0218","science",charset="utf8")

cousor=cnx.cursor()
sql_sentense="select * from url_content where place=5800058"
cousor.execute(sql_sentense)
str=''
list1=[]
for content in cousor.fetchall():
    str1=content[3]
    con_url=content[2]
    text = attatch_url(str1,con_url)
    url_list=text.get_couple_url()
    print url_list
    str2=text.Replace_Char(str1)

    for i in url_list:
        str2=str2.replace(i[0],i[1])
    print str2.encode('gbk','ignore')
t2=time.time()
print t2-t1
