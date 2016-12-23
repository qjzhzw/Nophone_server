from django.contrib import admin

from .models import information

class InformationAdmin(admin.ModelAdmin):
	list_display = ('identification', 'password', 'nickname', 'sex', 'birthday', 'constellation', 'hobby', 'email', 'motto', 'head')
	fieldsets = (
		['基本信息',{
			'fields':('identification', 'password'),
		}],
		['详细信息',{
			'fields': ('nickname', 'sex', 'birthday', 'constellation', 'hobby', 'email', 'motto', 'head'),
		}]
	)


admin.site.register(information, InformationAdmin)

# Register your models here.