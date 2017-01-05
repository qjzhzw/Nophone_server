# *-* coding: utf-8 *-*

from __future__ import unicode_literals

from django.db import models

class information(models.Model):
	identification = models.CharField('账号', max_length = 20)
	password = models.CharField('密码', max_length = 20)
	nickname = models.CharField('昵称', max_length = 20)
	sex = models.CharField('性别', max_length = 20)
	birthday = models.DateField('生日', default = '1970-1-1')
	constellation = models.CharField('星座', max_length = 20)
	hobby = models.CharField('爱好', max_length = 20)
	email = models.EmailField('邮箱')
	motto = models.CharField('签名', max_length = 20)
	head = models.ImageField('头像', upload_to = 'img')
	level = models.IntegerField('等级', default = 0)
	money = models.IntegerField('金币', default = 0)
	experience = models.IntegerField('经验', default = 0)
	def __unicode__(self):
		return self.identification
		
class goods(models.Model):
	name = models.CharField('商品名称', max_length = 20)
	address = models.CharField('店铺地址', max_length = 20)
	explanation = models.CharField('奖品说明', max_length = 20)
	price = models.IntegerField('金币', default = 0)
	picture = models.ImageField('图片', upload_to = 'img')
	def __unicode__(self):
		return self.name

# Create your models here.
