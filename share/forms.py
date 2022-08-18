from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.ModelForm):
	# identity = forms.CharField(max_length=254)

	class Meta():
		model = User
		fields = ('username', 'email', 'password')