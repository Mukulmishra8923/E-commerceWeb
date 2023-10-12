from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Costumer,profile_i
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class customerRegistrationForm(UserCreationForm):
 password1= forms.CharField(label='password' , widget=forms.PasswordInput(attrs= 
  {'class':'form-control'}))
 password2=forms.CharField(label="confirm password(again)", 
  widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email=forms.CharField(required=True ,widget=forms.EmailInput(attrs= 
  {'class':'form-control'}))

 
 class Meta: 
  model=User
  fields=['username','email','password1','password2']
  labels={'email':'Email'}
  widget={'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={"autofocus":True, 
   "class":'form-control'}))
    password= forms.CharField(label=_('password') , strip=False,
   widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'class':'form-control'}),)
  

class MyPasswordchangeForm(PasswordChangeForm):
 old_password=forms.CharField(label=_('Old password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True,
    'class':'form-control'}))
 new_password1=forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
    'class':'form-control'}))
 new_password2=forms.CharField(label=_('New password (again)'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
    'class':'form-control'}))
 


class MyPasswordResetForm(PasswordResetForm):
 email=forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={"autocomplete":"email","class":"form-control"})) 


class MySetPasswordForm(SetPasswordForm):
 new_password1=forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,
    'class':'form-control'}))
 new_password2=forms.CharField(label=_('New password (again)'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True,'class':'form-control'}))
  

class  CustomerProfileForm(forms.ModelForm):
  class Meta:
   model = Costumer
   fields = ['name','locality','city', 'state', 'zipcode']
   widget={'name':forms.TextInput(attrs={'class':'text-warning'}),
          'locality':forms.TextInput(attrs={'class':'form-control'}),
          'city':forms.TextInput(attrs={'class':'form-control'}),
          'state':forms.Select(attrs={'class':'form-control'}),
          'zipcode':forms.NumberInput(attrs={'class':'form-control'})}


class profile_imgForm(forms.ModelForm):
  class Meta:
    model=profile_i
    fields=['profile_pic','dp_name']
 