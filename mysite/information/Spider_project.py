# -*- coding:utf-8 -*-
# author :Max

import re
import urllib
import urllib2
import cookielib

from matplotlib.cbook import Null


#通过创建Spider类,用Spider类的两个方法来实现爬虫
class Spider:
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    def __init__(self,url,account,password,xnd,xqd):
        self.url = url
        self.account = account
        self.password = password
        self.xnd = xnd
        self.xqd = xqd
    def loginWeb(self):
        message = urllib2.urlopen(self.url).read()
        __ViewState = re.findall('<input type="hidden" name="__VIEWSTATE" value="(.*?)" />',message)

        if __ViewState == None:
            print 'no __VIewState'
            return
        headers = {'Connection': 'keep-alive','User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;Miser Report)'}
        data = urllib.urlencode({
            'TextBox1':self.account,'TextBox2':self.password,'RadioButtonList1':'ѧ��','Button1':'','__VIEWSTATE':__ViewState[0]})
        request = urllib2.Request(self.url,data,headers)
        try :
            response = Spider.opener.open(request).read().decode('gb2312').encode('utf-8')
            pattern = '<span id="xhxm">.*?  (.*?)同学</span></em>'
            # name = re.findall(pattern, response)
            # return name
        except urllib2.HTTPError,e:
            print 'HTTPError = '+e.code
            return 'Error'


    def timeTable(self):
        referer = 'http://jwxt.jiangnan.edu.cn/jndx/xs_main.aspx?xh='+self.account

        url = 'http://jwxt.jiangnan.edu.cn/jndx/xskbcx.aspx?xh=' + self.account + '&xm=%D6%DC%BF%C6%D3%F0&gnmkdm=N121603'

        headers = {'Connection': 'keep-alive','User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;Miser Report)','Referer':referer}
        request_test = urllib2.Request(url,headers= headers)
        message = Spider.opener.open(request_test).read().decode('gb2312','ignore').encode('utf-8')

        __ViewState = re.findall('<input type="hidden" name="__VIEWSTATE" value="(.*?)" />',message)
        # print __ViewState[0]
        # data = urllib.urlencode({'__EVENTTARGET':'xqd','__EVENTARGUMENT':'','__VIEWSTATE':__ViewState[0],
        #      'xnd':self.xnd,'xqd':self.xqd})
        #
        #
        # request = urllib2.Request(url,data,headers)
        # response = Spider.opener.open(request).read().decode('gb2312','ignore').encode('utf-8')
        # print response
        pattern = '<td align="Center".*?>(.*?)</td>'
        lessons = re.findall(pattern,message)

        lesson_name =[]
        lesson_classroom = []
        lesson_time = []
        for item in lessons:
            print item
            print len(item)
            if len(item) < 20:
                continue
            lesson_message =item.split("<br>")
            print lesson_message
            if lesson_message.__len__() > 7:
                #上课的名字、时间、教室分别储存在三个列表中
                lesson_name.append(lesson_message[0])
                lesson_time.appned(lesson_message[2])
                lesson_classroom.append(lesson_classroom[4])
                lesson_name.append(lesson_message[6])
                lesson_time.appned(lesson_message[8])
                lesson_classroom.append(lesson_classroom[10])

            else:
                lesson_name.append(lesson_message[0])
                lesson_time.append(lesson_message[2])
                lesson_classroom.append(lesson_classroom[4])

        for item in lesson_message:
            print item.name


        return
if __name__ == "__main__":
    print 'try spider'
    url = 'http://jwxt.jiangnan.edu.cn/jndx/default5.aspx'
    account = '1070414532'#学号
    password = '511623199512280018'#密码
    xnd = '2016-2017'#学年
    xqd = '2'#学期
    spider = Spider(url,account,password,xnd,xqd)
    name = spider.loginWeb()
    if name == 'Error':
        print 'Web Login Failed'
    else:
        print 'code right'
        spider.timeTable()
print 'run over'
    
