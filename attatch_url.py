# -*- coding: utf-8 -*-
import re

class attatch_url:
    ''' Need html content and the URL .Return attachment url.'''

    def __init__(self,htmlcontent=0,url=0):
        self.htmlcontent=htmlcontent
        self.url=url

    def get_attatch_url(self):
        '''主方法，返回attach_url'''

        att_url_list=[]

        att_url_1 = self.get_url(self.Replace_Char(self.htmlcontent))#干扰格式替换，获取url位置部分文本。
        for i in att_url_1:#生成附件所在url
            att_url_list.append(self.combin_url(self.get_domain(self.url,self.has_http(i)), i))
        return att_url_list

    def get_couple_url(self):

        att_couple=[]

        att_url_1 = self.get_url(self.Replace_Char(self.htmlcontent))
        for i in att_url_1:
            url_couple=[i,self.combin_url(self.get_domain(self.url,self.has_http(i)), i)]
            att_couple.append(url_couple)
        return att_couple

    #干扰格式替换
    def Replace_Char(self,htmlcon):
        # Regex_yinhao=re.compile(r'"')
        Regex_huanhang=re.compile(r'\r|\n|\t')
        Regex_5C=re.compile(r'%5C|(%E2%80%99)')
        Regex_22=re.compile(r'%22')
        # htmlcontent=re.sub(Regex_yinhao,"xxx",htmlcontent)
        newcontent=re.sub(Regex_huanhang,"",htmlcon)
        newcontent=re.sub(Regex_5C,"",newcontent)
        newcontent=re.sub(Regex_22,"",newcontent)

        return  newcontent

    #获取url的列表
    def get_url(self,htmlcon):
        content_list=[]
        Regex_b1=re.compile(ur'(<a(([^>]*?((\.(doc|xls|pdf|zip|jpg|png|rar|gzzf|7z)[^<]*?>)|(>\s*(<strong|<b|<span|<u|<img)?[^<]*\.(doc|xls|pdf|zip|jpg|png|rar|7z))))|([^<]*?((相关|打包|招标)?(附件|下载|文件|((招标|项目)(文件)))))).*?<)',re.I|re.U)
        q=re.findall(Regex_b1,htmlcon)
        if q:
            for i in q:
                content_list.append(i[0])
        Regex_href=re.compile(ur'<a[^>]*href="(.*?)"',re.I|re.U)#双引号
        Regex_href1=re.compile(ur"<a[^>]*href='(.*?)'",re.I|re.U)#单引号规则
        url_list=[]
        for str in content_list:
            m1 = re.match(Regex_href,str)
            n1 = re.match(Regex_href1,str)
            if m1:
                url_str= m1.group(1)
            elif n1:
                url_str= n1.group(1)
            else:
                url_str ='/#' #未发现href标签或连接内容为空
            url_list.append(url_str)

        return url_list  #返回url列表

    #识别获取url的格式
    def has_http(self,htmlcon):

        re_num=1  #斜杠或字符开头

        Regex_http=re.compile(ur'(http:|https:)',re.I|re.U)
        Regex_dian1=re.compile(ur'\.(\.)?/')
        m=re.match(Regex_http,htmlcon)
        m1=re.match(Regex_dian1,htmlcon)
        if m:
            re_num=0 #含有http:标志。
        elif m1:
            if m1.group(1):
                re_num=3  #两点
            else:
                re_num=2  #一点
        return re_num

    #传入url地址，根据规则获取所需url内容。
    def get_domain(self,url,re_num):

        Regex_getdomain=re.compile(ur'((http|https)://.*?)/',re.I|re.U)#wu dian
        Regex_getdomain1=re.compile(ur'((http|https)://.*)/.*?',re.I|re.U)# yi dian
        Regex_getdomain2=re.compile(ur'((http|https)://.*)/.*?/.*?',re.I|re.U) # liang dian
        m=re.match(Regex_getdomain,url)
        m1=re.match(Regex_getdomain1,url)
        m2=re.match(Regex_getdomain2,url)
        if m and re_num==1: #直接获取域名
            domain=m.group(1)
        elif m1 and re_num==2:
            domain=m1.group(1)
        elif m2 and re_num==3:
            domain=m2.group(1)
        else:
            domain=""  #若为0，则无需添加前部信息。

        return domain

    #根据规则合并url。
    def combin_url(self,domain,att_url):

        if att_url=='':
            return att_url

        elif self.has_http(att_url)==0:
            return att_url
        elif self.has_http(att_url)>=1:

            m=re.match(ur'\.?\.?(/.*)',att_url)
            if m:
                att_url=domain+m.group(1)
            else:
                att_url=domain+'/'+att_url

        return att_url

    def check(self):
        att_url_1 =self.Replace_Char(self.htmlcontent)
        Regex_a=re.compile(ur'\.(doc|xls|pdf|zip|rar|7z)',re.I|re.U)
        # Regex_a3=re.compile(ur'(<(a|A)[^>]*>\s?(附件|下载|文件|(招标|项目)文件))')
        m=re.search(Regex_a,att_url_1)
        # m3=re.search(Regex_a3,att_url_1)
        if m :
            return True
        else:
            return False



