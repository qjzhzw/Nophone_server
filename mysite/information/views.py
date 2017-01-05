# *-* coding: utf-8 *-*

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django import forms
import simplejson

from .models import information,goods
	
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


def register(request):
	if request.method == 'POST':
		data1 = request.POST['identification']#获取用户名
		data2 = request.POST['password']#获取密码
		result = information.objects.filter(identification = data1)
		
		data={}
		if(len(result) > 0):
			data['status'] = 'registered'
		else:
			user = information()
			user.identification = data1
			user.password = data2
			user.save()
			data['status'] = 'success'
		
		return HttpResponse(simplejson.dumps(data))


def register_information(request):
	if request.method == 'POST':
		flag = request.POST['identification']#获取用户名
		data1 = request.POST['nickname']#获取昵称
		data2 = request.POST['sex']#获取性别
		data3 = request.POST['birthday']#获取生日
		data4 = request.POST['constellation']#获取星座
		data5 = request.POST['hobby']#获取爱好
		data6 = request.POST['email']#获取邮箱
		data7 = request.POST['motto']#获取签名
		data8 = request.POST['head']#获取头像
		result = information.objects.filter(identification = flag).last()
		
		data={}
		try:
			result.nickname = data1
			result.sex = data2
			result.birthday = data3
			result.constellation = data4
			result.hobby = data5
			result.email = data6
			result.motto = data7
			result.head = data8
			result.save()
			data['status'] = 'success'
		except Exception, e:
			print e
			data['status'] = 'error'
		
		return HttpResponse(simplejson.dumps(data))


def login(request):
	if request.method == 'POST':
		data1 = request.POST['identification']#获取用户名
		data2 = request.POST['password']#获取密码
		result = information.objects.filter(identification = data1)#注意这里得到的是QuerySet类型
		
		data = {}
		if(len(result) == 0):
			data['status'] = 'not_existed'
		elif(cmp(result.last().password, data2) == 0):#这里得到的才是information类型
			data['status'] = 'success'
		else:
			data['status'] = 'not_matched'
		
		return HttpResponse(simplejson.dumps(data))


def user(request):
	if request.method == 'POST':
		flag = request.POST['identification']#获取用户名
		result = information.objects.filter(identification = flag).last()
		
		data = {}
		data['nickname'] = result.nickname
		data['sex'] = result.sex
		data['birthday'] = str(result.birthday)
		data['constellation'] = result.constellation
		data['hobby'] = result.hobby
		data['email'] = result.email
		data['motto'] = result.motto
		data['head'] = '111'
		data['level'] = result.level
		data['money'] = result.money
		data['experience'] = result.experience
		
		return HttpResponse(simplejson.dumps(data))


# Create your views here.
