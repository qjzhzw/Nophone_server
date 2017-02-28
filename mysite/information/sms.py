#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import httplib
import urllib
import random

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#账号
account  = "C53480005"
#密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "f5b97f315c97296ce309a7e36633f097"

def send_sms(text, mobile):
    params = urllib.urlencode({'account': account, 'password' : password, 'content': text, 'mobile':mobile,'format':'json' })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str 
	
def generate_verification_code():
    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))

    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片段返回
    verification_code = ''.join(myslice) # list to string
    # print code_list
    # print type(myslice)
    return verification_code
	
def send(identification):
	
    mobile = identification
    code = generate_verification_code()
    text = "您的验证码是：" + code + "。请不要把验证码泄露给其他人。"
	
    print(send_sms(text, mobile))
    return code