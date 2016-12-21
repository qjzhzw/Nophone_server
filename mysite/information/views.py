# *-* coding: utf-8 *-*

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django import forms
import simplejson

from .models import information
	
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


def send_information(request):

	if request.method == 'POST':
		data1 = request.POST['identification']#获取用户名
		data2 = request.POST['password']#获取密码
		user = information(identification = data1, password = data2)  
		user.save()
		return HttpResponse('success')
		
	if request.method == 'GET':
		data1 = request.GET['identification']#获取用户名
		data2 = request.GET['password']#获取密码
		user = information(identification = data1, password = data2)  
		user.save()
		return HttpResponse('success')


# Create your views here.
