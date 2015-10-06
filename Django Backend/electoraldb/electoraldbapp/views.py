from django.shortcuts import render
from django.http import HttpResponse
from electoraldbapp.forms import AddressForm,VoterForm,PartyForm,CandidateForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from electoraldbapp.models import Address,Constituency,Voter,Party,Candidate,Polling,ParliamentaryConstituency
from datetime import datetime
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.forms.models import model_to_dict
from time import time
import sys, traceback
from django.core import serializers
from django.db import connection

def encode(t):
	s = str(t)
	for i in range(0,8-len(s)):
		s = "0"+s
	return s
# Create your views here.
	# We make use of the shortcut function to make our lives easier.
def index(request):
	context = {}
	return render(request, 'electoraldb/index.html',context)

def add_voter(request):
	context = {}
	return render(request, 'electoraldb/add_voter.html',context)

def add_party(request):
	context = {}
	return render(request, 'electoraldb/add_party.html',context)

def add_candidate(request):
	try:
		acn = Constituency.objects.all()
		acno = []
		for x in acn:
			acno.append(x.acno)
	except Constituency.DoesNotExist:
		acno = None
	try:
		partys = Party.objects.all()
		pid = []
		for party in partys:
			if party.partyid != 'NO Party':
				pid.append(party.partyid)
	except Party.DoesNotExist:
		pid = None
	context = {'acno':acno,'pid':pid}
	return render(request, 'electoraldb/add_candidate.html',context)

def add_address(request):
	# ht
	
	if request.method == 'POST':
		data = request.POST
		try:
			acn = Constituency.objects.get(acno=data['acno'])
		except Constituency.DoesNotExist:
			acn = None
		form = AddressForm(request.POST)
		#is the form valid?
		if form.is_valid():						
			address = form.save(commit=False)
			print form
			address.acno = acn
			address.key = str(data['pin'])+":"+str(data['town'])
			address.save()
			return index(request)
		else:
			print form.errors
	else:
		#request was not post method type
		form = AddressForm()
	return render(request,'electoraldb/add_address.html',{'form':form})

def voter(request):
	if request.user.is_authenticated():
		v = Voter.objects.get(voterid=request.user.username)
		# print model_to_dict(v)
		return render(request,'electoraldb/voter.html',model_to_dict(v))
	else:
		return HttpResponseRedirect('/electoraldb/')

def party(request):
	if request.user.is_authenticated():
		p = Party.objects.get(partyid=request.user.username)
		candis = [x.candidateid for x in Candidate.objects.filter(partyid='NO Party')]
		candidates = [(x,Voter.objects.filter(voterid=x.voterid)[0],Constituency.objects.get(acno=x.acno)) for x in Candidate.objects.filter(partyid=p.partyid)]
		print candidates
		# print model_to_dict(p)
		return render(request,'electoraldb/party.html',{'party':p,'candis':candis,'candidates':candidates})
	else:
		return HttpResponseRedirect('/electoraldb/')

def candidate(request):
	if request.user.is_authenticated():
		c = Candidate.objects.get(candidateid=request.user.username)
		voter = Voter.objects.get(voterid=c.voterid)
		party = Party.objects.get(partyid=c.partyid)
		return render(request,'electoraldb/candidate.html',{'voter':voter,'candidate':c,'party':party})
	else:
		return HttpResponseRedirect('/electoraldb/')


def add_candi_party(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			print request.POST.get('cid')
			# add person to the party
			candi = Candidate.objects.get(candidateid=request.POST.get('cid'))
			candi.partyid = Party.objects.get(partyid=request.user.username)
			candi.save()
			return party(request)
		else:
			return party(request)
	else:
		return HttpResponseRedirect('/electoraldb/')

def voter_success(request):
	#render the success page and display voter details
	return render(request,'electoraldb/voter_success.html',{'Username':request.GET.get('username'),'Password':request.GET.get('password')})

def party_success(request):
	#render the success page and display voter details
	return render(request,'electoraldb/party_success.html',{'Username':request.GET.get('username'),'Password':request.GET.get('password')})

def candidate_success(request):
	#render the success page and display voter details
	return render(request,'electoraldb/candidate_success.html',{'Username':request.GET.get('username'),'Password':request.GET.get('password')})

def Logout(request):
	logout(request)
	return HttpResponseRedirect('/electoraldb/')

def Login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			# Is the account active? It could have been disabled.
			if user.is_active:
				if username.find("VW")!=-1:
					#session created
					login(request, user)
					return HttpResponseRedirect('/electoraldb/voter/')
				elif username.find("CI")!=-1:
					#session created
					login(request, user)
					return HttpResponseRedirect('/electoraldb/candidate')
				elif username.find("PI")!=-1:
					#session created
					login(request, user)
					return HttpResponseRedirect('/electoraldb/party/')
				else:
					return HttpResponse("Invalid Login Credentials")	
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print "Invalid login details: %s, %s"% (request.POST.get('username'),request.POST.get('password'))
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render(request, 'electoraldb/login.html', {})

def validate_candidate(request):
	# ht
	print "\nin the function add_candidate\n"
	if request.method == 'POST':
		form = CandidateForm(request.POST)
		if form.is_valid():
			print "\nform is_valid\n"
			candidate = form.save(commit=False)
			try:
				voter = Voter.objects.get(voterid=candidate.voterid)
			except:
				print "\nIncorrect VoterID\n"
				return HttpResponse("Voter ID does not exist !")				# render a proper message on UI
			candidate.candidateid = 'CI' + encode(Candidate.objects.count()+1)
			print "\nhere\n"
			user = User(username=candidate.candidateid,password=candidate.password)
			user.set_password(user.password)
			user.save()
			candidate.save()
			print "form: ",form
			return HttpResponseRedirect('/electoraldb/candidate_success/?username=%s&password=%s' %(candidate.candidateid,candidate.password))
		else:
			print "errors ",form.errors
	else:
		#request was not post method type
		form = CandidateForm()
	# to render 
	return HttpResponseRedirect('/electoraldb/add_candidate/')

def validate_party(request):
	# ht
	print "\nin the function\n"
	if request.method == 'POST': 	
		form = PartyForm(request.POST, request.FILES)
		if form.is_valid():
			print "\nis_valid\n"
			party = form.save(commit=False)
			party.partyid = 'PI' + encode(Party.objects.count()+1)
			print "\nhere\n"
			user = User(username=party.partyid,password=party.password)
			user.set_password(user.password)
			user.save()
			party.save()
			print "form: ",form
			return HttpResponseRedirect('/electoraldb/party_success/?username=%s&password=%s' %(party.partyid,party.password))
		else:
			print "errors ",form.errors
	else:
		#request was not post method type
		form = PartyForm()
	# to render 
	return render(request,'electoraldb/add_party.html',{'form':form})

def validate_voter(request):
	# ht
	
	if request.method == 'POST':
		data = request.POST
		print data
		form = VoterForm(request.POST)

		#print form
		#is the form valid?
		if form.is_valid():						
			voter = form.save(commit=False)
			voter.voterid = 'VW'+encode(Voter.objects.count()+1000)
			age = datetime.now().year - voter.dob.year 
			print age
			if age < 18:
				print "Enter age greater than 18"		# handle the front end here 
				return HttpResponse("Invalid Age : Age is less than 18")
			elif voter.town == '----':
				print "Enter Correct PIN" 	
				return HttpResponse("Invalid Age : Pin incorrect")			# handle the front end here
			else:
				user = User(username=voter.voterid,password=voter.password)
				user.set_password(user.password)
				user.save()
				i = datetime.now()
				voter.doa = str(i.year)+"-"+str(i.month)+"-"+str(i.day)
				voter.partno = Polling.objects.filter(town=voter.town)[0].partno
				voter.picno = "PICNO"
				voter.approved = 'false';
				voter.save()
				# print voter.town
				return HttpResponseRedirect('/electoraldb/voter_success/?username=%s&password=%s' %(voter.voterid,voter.password))
		else:
			print form.errors
	else:
		#request was not post method type
		form = VoterForm()
	return render(request,'electoraldb/add_voter.html',{'form':form})

def get_towns_from_pincode(request):
	try:
		if request.is_ajax():
			pincode = request.POST.get('pincode')
			response_data = {}
			print 'Yahan'
			addresses = Address.objects.filter(pin=pincode)

			towns = []
			for address in addresses:
				towns.append(address.town)

			response_data['towns'] = towns
			print pincode
			print towns
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
				)
		else:
			return HttpResponse(
				json.dumps({"nothing to see": "this isn't happening"}),
				content_type="application/json"
				)
	except Exception, e:
		logging.exception(e)
		raise e

def EC_login(request):
	Logout(request)
	return render(request,'electoraldb/EC_login.html',{});

def validate_EC(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			# user exists
			if user.username == 'admin':
				# login
				# session created
				login(request, user)
				return HttpResponseRedirect('/electoraldb/EC/')
			else:
				pass
		else:
			pass
	else:
		pass
	return HttpResponseRedirect('/electoraldb/EC_login/')

def approve_voter(request):
	if request.user.is_authenticated():
		# approve
		voters = request.POST.getlist('check[]')
		print voters
		for voterid in voters:
			voter = Voter.objects.get(voterid=voterid)
			voter.approved = 'true'
			i = datetime.now()
			voter.doi = str(i.year)+"-"+str(i.month)+"-"+str(i.day)
			voter.save()
		return HttpResponseRedirect('/electoraldb/EC/')
	else:
		return HttpResponseRedirect('/electoraldb/')


def approve_candidate(request):
	if request.user.is_authenticated():
		# approve
		candidates = request.POST.getlist('check[]')
		# print voters
		for candidateid in candidates:
			candidate = Candidate.objects.get(candidateid=candidateid)
			candidate.is_approved = True
			candidate.save()
		return HttpResponseRedirect('/electoraldb/EC/')
	else:
		return HttpResponseRedirect('/electoraldb/')


def approve_party(request):
	if request.user.is_authenticated():
		# approve
		parties = request.POST.getlist('check[]')
		for partyid in parties:
			party = Party.objects.get(partyid=partyid)
			party.is_approved = True
			party.save()
		return HttpResponseRedirect('/electoraldb/EC/')
	else:
		return HttpResponseRedirect('/electoraldb/')

def EC(request):
	if request.user.is_authenticated():
		# currently loggedin
		voters = [x for x in Voter.objects.filter(approved='false')]
		parties = [x for x in Party.objects.filter(is_approved=False)]
		candidates = [(x,Voter.objects.filter(voterid=x.voterid)[0],Constituency.objects.get(acno=x.acno)) for x in Candidate.objects.filter(is_approved=False)]
		print candidates
		return render(request,'electoraldb/EC.html',{'voters':voters,'parties':parties,'candidates':candidates})
	else:
		return HttpResponseRedirect('/electoraldb/')

def voter_search(request):
	try:
		if request.is_ajax() and request.user.is_authenticated() and request.user.username=='admin':
			voterid = request.POST.get('voterid')
			voter = Voter.objects.get(voterid=voterid);
			print voter;
			# print voter.as_json();
			returnval = serializers.serialize('json',[voter])
			return HttpResponse(json.dumps(returnval),content_type="application/json")
		else:
			return HttpResponse(
				json.dumps({"nothing to see": "this isn't happening"}),
				content_type="application/json"
				)
	except Exception, e:
		traceback.print_tb(file=sys.stdout)
		print 'Aha!! an excpetion'
		raise e

def voters_search(request):
	try:
		if request.is_ajax() and request.user.is_authenticated() and request.user.username=='admin':
			pincode = request.POST.get('pincode')
			town = request.POST.get('town')
			print pincode
			print town
			voters = Voter.objects.filter(pin=pincode,town=town)
			v = [(voter) for voter in voters];
			print v
			returnval = serializers.serialize('json',v)
			print returnval
			return HttpResponse(json.dumps(str(returnval)),
				content_type="application/json"
				)
		else:
			return HttpResponse(
				json.dumps({"nothing to see": "this isn't happening"}),
				content_type="application/json"
				)
	except Exception, e:
		traceback.print_tb(file=sys.stdout)
		raise e

def query(request):
	constituencies = Constituency.objects.all();
	acno = [constituency.acno for constituency in constituencies]
	candidates = Candidate.objects.all()
	cids = [candidate.candidateid for candidate in candidates]
	parties = Party.objects.all()
	pids = []
	for party in parties:
		if party.partyid != 'NO Party':
			pids.append(party.partyid)
	# global election data is drectly printed on this page	
	years = set()
	elections = global_elections()
	for election in elections:
		years.add(election[0])
	years = list(years)
	# print years
	return render(request,'electoraldb/query.html',{'acno':acno,'cids':cids,'pids':pids,'years':years})

def constituency(request):
	if request.method == 'POST':
		acno = request.POST.get('acno')
		constituency = Constituency.objects.get(acno=acno)
		pconstituency = ParliamentaryConstituency.objects.get(pcno=constituency.pcno)
		data = con_query(acno)
		return render(request,'electoraldb/constituency.html',{'constituency':constituency,'pconstituency':pconstituency,'data':data})
	else:
		return HttpResponseRedirect('/electoraldb/query/')

def candidate_details(request):
	if request.method == 'POST':
		c = Candidate.objects.get(candidateid=request.POST.get('cid'))
		voter = Voter.objects.get(voterid=c.voterid)
		party = Party.objects.get(partyid=c.partyid)

		return render(request,'electoraldb/candidate_details.html',{'voter':voter,'candidate':c,'party':party})
	else:
		return HttpResponseRedirect('/electoraldb/query/')

def con_query(acno):
	cur = connection.cursor()
	data = {}
	sql = "select Gender,Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"' Group By Gender"
	cur.execute(sql)
	x = cur.fetchall()
	print x
	data['female'] = 0
	data['male'] = 0
	for y in x:
		if y[0]=='female':
			data['female'] = y[1]
		else:
			data['male'] = y[1]

	sql = "select Caste,Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"' Group By Caste"
	cur.execute(sql)
	x = cur.fetchall()
	data['obc'] = 0
	data['sc'] = 0
	data['st'] = 0
	data['gen'] = 0
	for y in x:
		if y[0]=='OBC':
			data['obc'] = y[1]
		elif y[0]=='SC':
			data['sc'] = y[1]
		elif y[0]=='ST':
			data['st'] = y[1]
		else:
			data['gen'] = y[1]

	sql = "select Count(*) from Constituency Natural Join Polling Natural Join Voter where Acno='"+acno+"'"
	cur.execute(sql)
	data['population']=cur.fetchone()[0]
	print data
	return data

def party_stats(request):
	if request.method == 'POST':
		p = Party.objects.get(partyid=request.POST.get('pid'))
		# print model_to_dict(p)
		# get party election data
		pelections = party_elections(request.POST.get('pid'))
		print pelections
		candidates = [(x,Voter.objects.filter(voterid=x.voterid)[0],Constituency.objects.get(acno=x.acno)) for x in Candidate.objects.filter(partyid=p.partyid)]
		return render(request,'electoraldb/party_stats.html',{'party':p,'elections':pelections,'candidates':candidates})
	else:
		HttpResponseRedirect('/electoraldb/query/')

def elections(request):
	if request.method == 'POST':
		year = request.POST.get('year')
		yelections = global_election_query(year)
		return render(request,'electoraldb/elections.html',{'yelections':yelections,'year':year})
	else:
		HttpResponseRedirect('/electoraldb/query/')

def global_election_query(year):
	sql = "select Partyid,FemaleVotes+MaleVotes as votes from Election_Statistics Natural Join Election where year = "+str(year)+""
	cur = connection.cursor()
	cur.execute(sql)
	res = cur.fetchall()
	# print res

	dict1 = []
	for x in res:
		dict1.append((x[0],x[1]))

	# data['data']=dict1
	return dict1

def global_elections():
	sql = 'select year,FemaleVotes,MaleVotes,STVotes,SCVotes,OBCVotes,GENVotes,PartyName from Party natural join Election_Statistics natural join Election ORDER BY year'
	cur = connection.cursor()
	cur.execute(sql)
	res = cur.fetchall()
	print res
	data =[]
	for x in res:
		dict1 = []
		dict1.append(x[0])
		dict1.append(x[1])
		dict1.append(x[2])
		dict1.append(x[3])
		dict1.append(x[4])
		dict1.append(x[5])
		dict1.append(x[6])
		dict1.append(x[7])
		data.append(dict1)
	return data

def party_elections(partyid):
	sql = 'select year,FemaleVotes,MaleVotes,STVotes,SCVotes,OBCVotes,GENVotes,PartyName from Party natural join Election_Statistics natural join Election WHERE partyid="'+partyid+'" ORDER BY year'
	cur = connection.cursor()
	cur.execute(sql)
	res = cur.fetchall()
	print res
	data = []
	for x in res:
		dict1 = []
		dict1.append(x[0])
		dict1.append(x[1])
		dict1.append(x[2])
		dict1.append(x[3])
		dict1.append(x[4])
		dict1.append(x[5])
		dict1.append(x[6])
		dict1.append(x[7])
		data.append(dict1)
	return data
