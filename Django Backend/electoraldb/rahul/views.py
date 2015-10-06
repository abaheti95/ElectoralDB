from django.shortcuts import render
from django.http import HttpResponse
from electoraldbapp.forms import AddressForm,VoterForm, PartyForm, CandidateForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from electoraldbapp.models import Address,Constituency,Voter,Party, Candidate
from datetime import datetime
from datetime import datetime

def encode(t):
	s = str(t)
	for i in range(0,8-len(s)):
		s = "0"+s
	return s
# Create your views here.
# We make use of the shortcut function to make our lives easier.
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context = {}
    return render(request, 'electoraldb/index.html',context)	


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
			address.save()
			return index(request)
		else:
			print form.errors
	else:
		#request was not post method type
		form = AddressForm()
	return render(request,'electoraldb/add_address.html',{'form':form})


def add_voter(request):
	# ht
	
	if request.method == 'POST':
		data = request.POST
		print data
		form = VoterForm(request.POST)
		#print form
		#is the form valid?
		if form.is_valid():						
			voter = form.save(commit='False')
			voter.voterid = 'VW'+encode(Voter.objects.count()+1)
			i = datetime.now()
			voter.doa = str(i.year)+"-"+str(i.month)+"-"+str(i.day)
			voter.partno = 'NEWPART'
			voter.picno = "PICNO"
			voter.save()
			return index(request)
		else:
			print form.errors
	else:
		#request was not post method type
		form = VoterForm()
	return render(request,'electoraldb/add_voter.html',{'form':form})

def add_party(request):
	# ht
	if request.method == 'POST': 	
		data = request.POST
		form = PartyForm(request.POST)
		#is the form valid?
		if form.is_valid():
			party = form.save(commit=False)
			print form
			party.partyid = 'PI' + encode(Party.objects.count()+1)
			party.save()
			return index(request)
		else:
			print form.errors
	else:
		#request was not post method type
		form = PartyForm()
	return render(request,'electoraldb/add_party.html',{'form':form})

def add_candidate(request):
	# ht
	if request.method == 'POST': 	
		data = request.POST
		form = CandidateForm(request.POST)
		#is the form valid?
		if form.is_valid():
			candidate = form.save(commit=False)
			print form
			candidate.candidateid = 'CI' + encode(Candidate.objects.count()+1)
			candidate.save()
			return index(request)
		else:
			print form.errors
	else:
		#request was not post method type
		form = CandidateForm()
	return render(request,'electoraldb/add_candidate.html',{'form':form})