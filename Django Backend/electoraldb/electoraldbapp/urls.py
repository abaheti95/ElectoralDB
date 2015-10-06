from django.conf.urls import patterns,url
from electoraldbapp import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
	url(r'^$', views.index, name=''),
	url(r'^index.html', views.index, name='index.html'),
	url(r'^index/$', views.index, name='index'),
	url(r'^query/$', views.query, name='query'),
	url(r'^constituency/$', views.constituency, name='constituency'),
	url(r'^candidate_details/$', views.candidate_details, name='candidate_details'),
	url(r'^party_stats/$', views.party_stats, name='party_stats'),
	url(r'^elections/$', views.elections, name='elections'),
	# url(r'^home/', TemplateView.as_view(template_name='electoraldb/base.html'),
	# url(r'^add_address/$', views.add_address, name='add_address'),
	url(r'^EC/$', views.EC, name='EC'),
	url(r'^EC_login/$', views.EC_login, name='EC_login'),
	url(r'^validate_EC/$', views.validate_EC, name='validate_EC'),
	url(r'^approve_voter/$', views.approve_voter, name='approve_voter'),
	url(r'^approve_candidate/$', views.approve_candidate, name='approve_candidate'),
	url(r'^approve_party/$', views.approve_party, name='approve_party'),
	# Ajax pages for ec
	url(r'^voter_search/$', views.voter_search, name='voter_search'),
	url(r'^voters_search/$', views.voters_search, name='voters_search'),
	

	url(r'^add_candi_party/$', views.add_candi_party, name='add_candi_party'),
	url(r'^login/$', views.Login, name='login'),
	url(r'^logout/$', views.Logout, name='logout'),
	url(r'^candidate/$', views.candidate, name='candidate'),
	url(r'^add_candidate/$', views.add_candidate, name='add_candidate'),
	url(r'^validate_candidate/$', views.validate_candidate, name='validate_candidate'),
	url(r'^candidate_success/$', views.candidate_success, name='candidate_success'),
	url(r'^party/$', views.party, name='party'),
	url(r'^add_party/$', views.add_party, name='add_party'),
	url(r'^validate_party/$', views.validate_party, name='validate_party'),
	url(r'^party_success/$', views.party_success, name='party_success'),
	url(r'^voter/$', views.voter, name='voter'),
	url(r'^add_voter/$', views.add_voter, name='add_voter'),
	url(r'^validate_voter/$', views.validate_voter, name='validate_voter'),
	url(r'^voter_success/$', views.voter_success, name='voter_success'),
	url(r'^town_from_pin/$',views.get_towns_from_pincode, name='town_from_pin')
	)