from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField()
	password = forms.CharField()

	def clean(self):
		return self.cleaned_data 

	def save(self):
		signup = User.objects.create_user(**self.cleaned_data)
		signup.save()
		return signup
