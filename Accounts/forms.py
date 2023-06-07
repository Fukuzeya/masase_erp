from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from Applicant.models import EmploymentDetails
from Agent.models import Agent

class ClientSignUp(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        id = EmploymentDetails.objects.filter(employee_number= first_name)
        if id.count() ==0:
            raise forms.ValidationError("Your ec number is not recognised!")
        return first_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})


class AgentSignUp(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        id = Agent.objects.filter(national_id= first_name)
        if id.count() ==0:
            raise forms.ValidationError("Your national id is not recognised!")
        return first_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})
        
        
# class TeacherSignUp(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['username', 'first_name','password1','password2']

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         r = User.objects.filter(username=username)
#         if r.count():
#             raise forms.ValidationError("Username already exists")
#         return username

#     def clean_first_name(self):
#         first_name = self.cleaned_data['first_name']
#         id = Teacher.objects.filter(ec_number= first_name)
#         if id.count() ==0:
#             raise forms.ValidationError("Your ec number is not recognised!")
#         return first_name

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError('Passwords do not match.')
#         return cd['password2']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update(
#             {'class': 'form-control','Label':'Username','Placeholder':'Your username'})
#         self.fields['first_name'].widget.attrs.update(
#             {'class': 'form-control','Label':'National Id','Placeholder':'Your national ID'})
#         self.fields['password1'].widget.attrs.update(
#             {'class': 'form-control','Placeholder':'Your password'})
#         self.fields['password2'].widget.attrs.update(
#             {'class': 'form-control','Placeholder':'Confirm your password'})

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
