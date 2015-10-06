from django import forms
from electoraldbapp.models import Party, Candidate
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import html5.forms.widgets as html5_widgets

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 

class PartyForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.widgets.PasswordInput, label = "Password")
	password2 = forms.CharField(widget=forms.widgets.PasswordInput, label = "Confirm Password")

 	class Meta:
         model = Party
         fields = ('partyname','symbol','type','password1','password2')
	
	def clean(self):
		cleaned_data = super(PartyForm,self).clean()

		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1']!=self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
		return self.cleaned_data

	def save(self, commit = True):
		user = super(PartyForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

class CandidateForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.widgets.PasswordInput, label = "Password")
	password2 = forms.CharField(widget=forms.widgets.PasswordInput, label = "Confirm Password")

 	class Meta:
         model = Candidate
         fields = ('voterid','acno','type','partyid','password1','password2')
	
	def clean(self):
		cleaned_data = super(CandidateForm,self).clean()

		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1']!=self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
		return self.cleaned_data

	def save(self, commit = True):
		user = super(CandidateForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class AuthenticationForm(forms.Form):
	"""
	Login form
	"""
	partyid = forms.CharField(widget=forms.widgets.TextInput)
	password = forms.CharField(widget=forms.widgets.PasswordInput)

	class Meta:
		fields = ['partyid', 'password']