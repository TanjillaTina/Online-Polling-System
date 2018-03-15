from django import forms
from polling.models import SetChoices,Voter,MyAdmin
from django.core.exceptions import ValidationError
from django.core import validators




'''
class AdminLogin(forms.ModelForm):
	class Meta:
		model = MyAdmin
		fields='__all__'
	def clean_user_name(self):
		user_name = self.cleaned_data['user_name']

		if MyAdmin.objects.filter(user_name=user_name).count() > 0:
			raise ValidationError("Incorrect User Name")
		return user_name

	def clean_password(self):
		password = self.cleaned_data['password']

		if MyAdmin.objects.filter(password=password).count() > 0:
			raise ValidationError("Incorrect Password")
		return password
'''
class ChoiceForm(forms.ModelForm):
	class Meta:
		model = SetChoices
		fields='__all__'


class VoterForm(forms.ModelForm):
	class Meta:
		model=Voter
		fields='__all__'
			

class AdminForm(forms.Form):
	name=forms.CharField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)



