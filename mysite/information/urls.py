from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^register/', views.register, name='register'),
	url(r'^register_information/', views.register_information, name='register_information/'),
	url(r'^login/', views.login, name='login'),
	url(r'^user/', views.user, name='user'),
]