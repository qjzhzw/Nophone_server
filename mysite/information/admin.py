from django.contrib import admin

from .models import information,goods,phone

class InformationAdmin(admin.ModelAdmin):
	list_display = ('identification', 'password', 'nickname', 'level', 'money', 'experience', 'head')
	fieldsets = (
		['基本信息',{
			'fields':('identification', 'password'),
		}],
		['个人信息',{
			'fields': ('nickname', 'sex', 'birthday', 'constellation', 'hobby', 'email', 'motto', 'head'),
		}],
		['账号信息',{
			'fields': ('level', 'money', 'experience'),
		}],
	)
	
class GoodsAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'explanation', 'price', 'picture')
	fieldsets = (
		['商品信息',{
			'fields':('name', 'address', 'explanation', 'price', 'picture'),
		}],
	)
	
class PhoneAdmin(admin.ModelAdmin):
	list_display = ('identification', 'code')
	fieldsets = (
		['验证码信息',{
			'fields':('identification', 'code'),
		}],
	)

admin.site.register(information, InformationAdmin)
admin.site.register(goods, GoodsAdmin)
admin.site.register(phone, PhoneAdmin)

# Register your models here.