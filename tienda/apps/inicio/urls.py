from django.conf.urls import patterns, url, include
from views import ProductView, ContactView

#URLS DE LA APLICACION INICIO
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view( template_name='inicio/index.html' ) , name="home"),
	#url(r'^$',, {'template_name': 'inicio/index.html'} , name="login"),
	url(r'^about/$',TemplateView.as_view( template_name='inicio/about.html' ) , name="about"),
	url(r'^product/$',ProductView.as_view() , name="product"),
	url(r'^contact/$',ContactView.as_view() , name="contact"),
	url(r'^$','django.contrib.auth.views.login', {'template_name': 'inicio/login.html'} , name="login"),
	url(r'^logout/$','django.contrib.auth.views.logout_then_login' , name="logout"),
)