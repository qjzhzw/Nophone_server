# *-* coding: utf-8 *-*

from __future__ import unicode_literals

from django.db import models

class information(models.Model):
	identification = models.IntegerField('账号')
	password = models.CharField('密码', max_length = 20)
	nickname = models.CharField('昵称', max_length = 20, default = '我的昵称')
	sex = models.CharField('性别', max_length = 20, default = '汉子')
	birthday = models.DateField('生日', default = '1970-1-1')
	constellation = models.CharField('星座', max_length = 20, default = '白羊座')
	hobby = models.CharField('爱好', max_length = 20)
	email = models.EmailField('邮箱')
	motto = models.CharField('签名', max_length = 20, default = '您尚未设置签名')
	head = models.FileField('头像', upload_to = 'static/head')
	level = models.IntegerField('等级', default = 1)
	money = models.IntegerField('金币', default = 0)
	experience = models.IntegerField('经验', default = 0)
	def __unicode__(self):
		return str(self.identification)
		
class goods(models.Model):
	name = models.CharField('商品名称', max_length = 20)
	address = models.CharField('店铺地址', max_length = 20)
	explanation = models.CharField('奖品说明', max_length = 20)
	price = models.IntegerField('金币', default = 0)
	picture = models.FileField('图片', upload_to = 'static/goods')
	def __unicode__(self):
		return self.name
		
class phone(models.Model):
	identification = models.IntegerField('手机号')
	code = models.CharField('验证码', max_length = 6)
	def __unicode__(self):
		return str(self.identification)

# Create your models here.
