from django import forms

class RegisterForm(forms.Form):
	username = 			forms.CharField(max_length=30)
	email =             forms.EmailField()
	password =          forms.CharField(max_length=30, widget=forms.PasswordInput())
	verify_password =   forms.CharField(max_length=30, widget=forms.PasswordInput())
	eula =              forms.BooleanField()