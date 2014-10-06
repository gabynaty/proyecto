from  django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UsuarioForm(forms.Form):
	class Meta:
		form=User
		exclude=["username"]
