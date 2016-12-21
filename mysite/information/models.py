# *-* coding: utf-8 *-*

from __future__ import unicode_literals

from django.db import models

class information(models.Model):
	identification = models.CharField('账号', max_length=50)
	password = models.CharField('密码', max_length=50)
	def __unicode__(self):
		return '账号：' + self.identification + ' 密码：' + self.password

# Create your models here.
