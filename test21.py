# -*- coding: utf-8 -*-
import re
from attatch_url import attatch_url
import time

# 正则结构测试。
t1=time.time()
str=u'''一点规则：<a href="./zfcg/201510/201510933392511.doc">HZYHZFCG-2015-365.doc</a>
        两点规则：<a href="../zfcg/20110/2511.doc">HZYHZFCG-2015-365.doc.doc</a>
        斜杠：<a href="/zfcg/201/920392511.doc.doc.pdf">HZYHZFCG-2015-365.doc</a>
        字母：<a href="zfcg01510/P02015100933.doc">HZYHZFCG-2015-365.doc</a>
        后缀名在页面中：<a href="/zfcg/2015/009338920392511">   <strong>HZYHZFCG-2015-36.doc</strong></a>
        无后缀名，关键字：<a href="/zfcg/201510/P02511">下载</a>
        无链接：<a href=""><strong>HZYHZFCG-2015-36.doc</strong></a>'''
con_url='http://www.mysql.com/123/456/789/this.html'

text = attatch_url(str,con_url)
url_list=text.get_couple_url()

print url_list,len(url_list)
str1=text.Replace_Char(str)

for i in url_list:
    if i[0]!=i[1]:
        str1=str1.replace(i[0],i[1])
print str1
t2=time.time()
print t2-t1