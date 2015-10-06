from django import forms
from electoraldbapp.models import Address, Constituency, Voter, Polling, Party
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import html5.forms.widgets as html5_widgets

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 
def encode(t):
	s = str(t)
	for i in range(0,8-len(s)):
		s = "0"+s
	return s

class AddressForm(forms.ModelForm):
	pin = forms.IntegerField(help_text="Please enter the pincode",required=False)# Field name made lowercase.
	po = forms.CharField(max_length=20,help_text="Post office?")  # Field name made lowercase.
	town = forms.CharField(max_length=50,help_text="Town?")  # Field name made lowercase.
	district = forms.CharField(max_length=50,help_text="District?")  # Field name made lowercase.
	state = forms.CharField(max_length=50,help_text="state?")  # Field name made lowercase.
	acno = forms.ModelChoiceField(queryset=Constituency.objects.all(),help_text="Select the constituency")  # Field name made lowercase.
	key = forms.CharField(help_text="What is your aim?")
	class Meta:
		model = Address
		fields = ('pin','po','town','district','state','acno',)
	#  	
class VoterForm(forms.ModelForm):
	name = forms.CharField(max_length=50,help_text="Enter your name:")
    password = forms.CharField(widget=forms.PasswordInput())
	# Field name made lowercase.
	age = forms.IntegerField(validators=[MinValueValidator(18)],help_text="Enter your age")  # Field name made lowercase.
	gender = forms.ChoiceField(label=u'sex', choices=[('Male','Male'),('Female','Female'),('Other','Other')], widget=forms.Select(), required=False,help_text="Enter your gender:")
	pin = forms.CharField(max_length = 30,help_text = "fill this one")
	town = forms.CharField(max_length = 30,help_text = "fill this one for town")
	dob = forms.DateField(help_text="Birth Date:")  # Field name made lowercase.
	emailid = forms.EmailField(max_length=100,help_text="Enter your emailid:")  # Field name made lowercase.
	phoneno = forms.IntegerField(help_text="Enter your phoneno:")  # Field name made lowercase.
	houseno = forms.IntegerField(help_text="Enter your houseno:")  # Field name made lowercase.
	streetno = forms.CharField(max_length=20,help_text="Enter your streetno:")  # Field name made lowercase.
	#pin = forms.ModelChoiceField(queryset=Address.objects.all(),help_text="Select your pin code:")  # Field name made lowercase.
	#town = forms.ModelChoiceField(queryset=Address.objects.all(),help_text="Select your town:")  # Field name made lowercase.
	caste = forms.ChoiceField(label='Caste',choices=[('ST','Scheduled Tribe'),('SC','Scheduled Caster'),('OBC','Other Backward Classes'),('GEN','General')],help_text="Enter your caste:")  # Field name made lowercase.
	#partno = forms.CharField(initial = 0,help_text="Part no")
	# def clean(self):
	# 	dob = self.cleaned_data['dob']
	# 	today = datetime.date.today()
	# 	if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
	# 		raise forms.ValidationError('Must be at least 18 years old to register')
	# 	return dob
	class Meta:
		model = Voter
		fields = ('name','age','gender','dob','emailid','phoneno','houseno','streetno','caste')
		#exclude = ('voterid','doa','doi','picno','partno',)


