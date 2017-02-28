from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^register/', views.register, name='register'),
	url(r'^vertification/', views.vertification, name='vertification'),
	url(r'^register_information/', views.register_information, name='register_information/'),
	url(r'^login/', views.login, name='login'),
	url(r'^user/', views.user, name='user'),
	url(r'^market_information/', views.market_information, name='market_information/'),
	url(r'^market_goods/', views.market_goods, name='market_goods/'),
	url(r'^goods_information/', views.goods_information, name='goods_information/'),
	url(r'^goods_change/', views.goods_change, name='goods_change/'),
	url(r'^course/', views.course, name='course/'),
	url(r'^tree/', views.tree, name='tree/'),
	url(r'^tree_water/', views.tree_water, name='tree_water/'),
]