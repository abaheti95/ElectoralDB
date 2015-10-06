from django.shortcuts import render
from django.http import HttpResponse
from electoraldbapp.forms import AddressForm,VoterForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from electoraldbapp.models import Address,Constituency,Voter
from datetime import datetime
from datetime import datetime
#from django.core.serializers import json
import json
from django.views.decorators.csrf import ensure_csrf_cookie


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
			address.key = str(data['pin'])+":"+str(data['town'])
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
			voter = form.save(commit=False)
			voter.voterid = 'VW'+encode(Voter.objects.count()+1)
			i = datetime.now()
			voter.doa = str(i.year)+"-"+str(i.month)+"-"+str(i.day)
			voter.partno = 'NEWPART'
			voter.picno = "PICNO"			
			x =  Address.objects.get(pin=data['pin'],town=data['town'])
			print x
			voter.pin = Address.objects.get(pin=data['pin'],town=data['town'])
			voter.town =Address.objects.get(pin=data['pin'],town=data['town'])
			voter.save()
			print voter.town.town
			return index(request)
		else:
			print form.errors
	else:
		#request was not post method type
		form = VoterForm()
	return render(request,'electoraldb/add_voter.html',{'form':form})

def validate_candidate(request):
	if request.method == 'POST':
		data = request.POST
		print data
		form = VoterForm(request.POST)
		#print form
		#is the form valid?
		if form.is_valid():						
			voter = form.save(commit=False)
			voter.voterid = 'VW'+encode(Voter.objects.count()+1)
			i = datetime.now()
			voter.doa = str(i.year)+"-"+str(i.month)+"-"+str(i.day)
			voter.partno = 'NEWPART'
			voter.picno = "PICNO"			
			x =  Address.objects.get(pin=data['pin'],town=data['town'])
			print x
			voter.pin = Address.objects.get(pin=data['pin'],town=data['town'])
			voter.town =Address.objects.get(pin=data['pin'],town=data['town'])
			voter.save()
			print voter.town.town
			return index(request)
		else:
			print form.errors
	else:
		#agar koi hacker hoo toh
		pass
	return render(request,'electoraldb/candidate.html')


def get_towns_from_pincode(request):
	try:
		if request.is_ajax():
			pincode = request.POST.get('pincode')
			response_data = {}

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