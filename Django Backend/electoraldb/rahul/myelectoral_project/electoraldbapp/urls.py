from django.conf.urls import patterns,url
from electoraldbapp import views
urlpatterns = patterns('',
   	url(r'^$', views.index, name='index'),
    # url(r'^add_address/$', views.add_address, name='add_address'),
    # url(r'^add_voter/$', views.add_voter, name='add_voter'),
   	# url(r'^show_party/$', views.add_voter, name='add_voter'), 
    url(r'^add_party/$', views.add_party, name='add_party'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^add_candidate/$', views.add_candidate, name='add_candidate'),
    # url(r'^add_candidate/$', views.add_candidate, name='add_candidate'),
    )