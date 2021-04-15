from django import forms
from .models import Student_user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class Signup_form(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        labels = {'first_name':'First Name', 'last_name':'Last Name','email':'Email'}
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class Login_form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))
    


class Student(forms.ModelForm):
    class Meta:
        model = Student_user
        fields = ['name', 'email', 'phone', 'location']
        labels = {'name':'Name', 'email':'Email', 'phone':'Mobile no.','location':'Location'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
        }
