from django.db.models.signals import post_save, pre_save
from django import forms
from django.dispatch import  receiver
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=200,required = True,help_text='Enter Username',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),) 
    email = forms.EmailField(max_length=50, required=True, help_text='Enter Email Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    flat_no = forms.CharField(max_length=20, required=True, help_text='Enter Flat Number',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Flat Number'}),)
    tower_no = forms.CharField(max_length=20, required=True, help_text='Enter Tower Number',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tower Number'}),)
    phone_no = forms.IntegerField(max_value=10000000000, required=True, help_text='Enter Phone Number',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),)
    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)

class Meta:
    model = User
    fields = ['email', 'flat_no', 'tower_no', 'phone_no', 'password1', 'password2',]
