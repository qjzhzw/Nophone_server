#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import httplib
import urllib
import random

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#�˺�
account  = "C53480005"
#���� �鿴�������¼�û�����->��֤�롢֪ͨ����->�ʻ���ǩ������->APIKEY
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
    ''' �������6λ����֤�� '''
    code_list = []
    for i in range(10): # 0-9����
        code_list.append(str(i))

    myslice = random.sample(code_list, 6)  # ��list�������ȡ6��Ԫ�أ���Ϊһ��Ƭ�η���
    verification_code = ''.join(myslice) # list to string
    # print code_list
    # print type(myslice)
    return verification_code
	
def send(identification):
	
    mobile = identification
    code = generate_verification_code()
    text = "������֤���ǣ�" + code + "���벻Ҫ����֤��й¶�������ˡ�"
	
    print(send_sms(text, mobile))
    return code