from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^register/', views.register, name='register'),
	url(r'^register_information/', views.register_information, name='register_information/'),
	url(r'^login/', views.login, name='login'),
	url(r'^user/', views.user, name='user'),
	url(r'^market_information/', views.market_information, name='market_information/'),
	url(r'^market_goods/', views.market_goods, name='market_goods/'),
]