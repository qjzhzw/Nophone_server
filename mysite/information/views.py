# *-* coding: utf-8 *-*

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django import forms
import simplejson
import sms

from .models import information,goods,phone
	
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def vertification(request):
	if request.method == 'POST':
		data_identification = request.POST['identification']#获取用户名
		
		get_code = sms.send(data_identification)#发送验证码
		user = phone()
		user.identification = data_identification
		user.code = get_code
		user.save()
		
		data = {}
		data['status'] = 'success'
		
		return HttpResponse(simplejson.dumps(data))

def register(request):
	if request.method == 'POST':
		data_identification = request.POST['identification']#获取用户名
		data_password = request.POST['password']#获取密码
		data_vertification = request.POST['vertification']#获取验证码
		result_information = information.objects.filter(identification = data_identification)
		result_phone = phone.objects.filter(identification = data_identification)
		
		data={}
		if(len(result_information) > 0):
			data['status'] = 'registered'
		elif(cmp(result_phone.last().code, data_vertification) != 0):
			data['status'] = 'error'
		else:
			user = information()
			user.identification = data_identification
			user.password = data_password
			user.save()
			data['status'] = 'success'
		
		return HttpResponse(simplejson.dumps(data))

base_url = 'http://qjzhzw.tunnel.qydev.com/'

def register_information(request):
	if request.method == 'POST':
		flag_identification = request.POST['identification']#获取用户名
		data_nickname = request.POST['nickname']#获取昵称
		data_sex = request.POST['sex']#获取性别
		data_birthday = request.POST['birthday']#获取生日
		data_constellation = request.POST['constellation']#获取星座
		data_hobby = request.POST['hobby']#获取爱好
		data_email = request.POST['email']#获取邮箱
		data_motto = request.POST['motto']#获取签名
		data_head = request.POST['head']#获取头像
		result = information.objects.filter(identification = flag_identification).last()
		
		data={}
		try:
			result.nickname = data_nickname
			result.sex = data_sex
			result.birthday = data_birthday
			result.constellation = data_constellation
			result.hobby = data_hobby
			result.email = data_email
			result.motto = data_motto
			result.head = data_head
			result.save()
			data['status'] = 'success'
		except Exception, e:
			print e
			data['status'] = 'error'
		
		return HttpResponse(simplejson.dumps(data))


def login(request):
	if request.method == 'POST':
		data_identification = request.POST['identification']#获取用户名
		data_password = request.POST['password']#获取密码
		result = information.objects.filter(identification = data_identification)#注意这里得到的是QuerySet类型
		
		data = {}
		if(len(result) == 0):
			data['status'] = 'not_existed'#用户名不存在
		elif(cmp(result.last().password, data_password) == 0):
			data['status'] = 'success'
		else:
			data['status'] = 'not_matched'#密码输入错误
		
		return HttpResponse(simplejson.dumps(data))


def user(request):
	if request.method == 'POST':
		flag_identification = request.POST['identification']#获取用户名
		result = information.objects.filter(identification = flag_identification).last()
		
		data = {}
		data['nickname'] = result.nickname
		data['sex'] = result.sex
		data['birthday'] = str(result.birthday)
		data['constellation'] = result.constellation
		data['hobby'] = result.hobby
		data['email'] = result.email
		data['motto'] = result.motto
		data['level'] = result.level
		data['money'] = result.money
		data['experience'] = result.experience
		try:
			data['head'] = base_url + result.head.url
		except Exception, e:
			data['head'] = base_url + 'static/head/wolf.png'
		
		return HttpResponse(simplejson.dumps(data))


def market_information(request):
	if request.method == 'POST':
		flag_identification = request.POST['identification']#获取用户名
		result = information.objects.filter(identification = flag_identification).last()
		
		data = {}
		data['nickname'] = result.nickname
		data['level'] = result.level
		data['money'] = result.money
		data['experience'] = result.experience
		try:
			data['head'] = base_url + result.head.url
		except Exception, e:
			data['head'] = base_url + 'static/head/wolf.png'
		
		return HttpResponse(simplejson.dumps(data))


def market_goods(request):
	if request.method == 'POST':
#		number = request.POST['number']#获取个数
		result = goods.objects.filter().all()
		number = len(result)
		
		data = {}
		data['number'] = number
		for i in range(0,int(number)):
			content = {}
			content['name'] = result[len(result) - i - 1].name
			content['address'] = result[len(result) - i - 1].address
			content['explanation'] = result[len(result) - i - 1].explanation
			content['price'] = result[len(result) - i - 1].price
			content['picture'] = base_url + result[len(result) - i - 1].picture.url
			data['goods' + str(i + 1)] = content
		
		return HttpResponse(simplejson.dumps(data))


def goods_information(request):
	if request.method == 'POST':
		flag_name = request.POST['name']#获取商品名称
		result = goods.objects.filter(name = flag_name).last()
		
		data = {}
		data['address'] = result.address
		data['explanation'] = result.explanation
		data['price'] = result.price
		data['picture'] = base_url + result.picture.url
		
		return HttpResponse(simplejson.dumps(data))
		
		
def goods_change(request):
	if request.method == 'POST':
		data_identification = request.POST['identification']#获取用户名
		result_information = information.objects.filter(identification = data_identification).last()
		data_name = request.POST['name']#获取商品名称
		result_goods = goods.objects.filter(name = data_name).last()
		
		data={}
		if result_information.money - result_goods.price < 0:
			data['status'] = 'not enough'#余额不足
		else:
			result_information.money -= result_goods.price
			result_information.save()
			data['status'] = 'success'#兑换商品成功
		
		return HttpResponse(simplejson.dumps(data))
		
		
def course(request):
	if request.method == 'POST':
		data_identification = request.POST['identification']#获取学号
		data_password = request.POST['password']#获取密码
		
		data={}
		try:
			print flag1
			data['status'] = 'success'
		except Exception, e:
			print e
			data['status'] = 'error'
		
		return HttpResponse(simplejson.dumps(data))
		
		
def tree(request):
	if request.method == 'POST':
		flag_identification = request.POST['identification']#获取用户名
		result = information.objects.filter(identification = flag_identification).last()
		
		data={}
		data['level'] = result.level
		
		return HttpResponse(simplejson.dumps(data))
		
		
def tree_water(request):
	if request.method == 'POST':
		flag_identification = request.POST['identification']#获取用户名
		result = information.objects.filter(identification = flag_identification).last()
		result.experience += 1
		result.save()
		
		data={}
		try:
			data['status'] = 'success'
		except Exception, e:
			print e
			data['status'] = 'error'
		
		return HttpResponse(simplejson.dumps(data))


# Create your views here.
