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
		result = information.objects.filter(identification = data1)
		
		data={}
		if(len(result) > 0):
			data['status'] = 'registered'
			return HttpResponse(simplejson.dumps(data))
		else:
			user = information()
			user.identification = data1
			user.password = data2
			user.birthday = '1970-1-1'
			user.save()
			data['status'] = 'success'
			return HttpResponse(simplejson.dumps(data))


# Create your views here.
