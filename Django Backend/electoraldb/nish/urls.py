from django.conf.urls import patterns,url
from electoraldbapp import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# url(r'^home/', TemplateView.as_view(template_name='electoraldb/base.html'),
	url(r'^add_address/$', views.add_address, name='add_address'),
	url(r'^add_voter/$', views.add_voter, name='add_voter'),
	url(r'^town_from_pin/$',views.get_towns_from_pincode, name='town_from_pin')
	)