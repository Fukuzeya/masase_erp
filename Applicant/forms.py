from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)


from .models import *

#Applicant Form 1
class ApplicationForm1(forms.ModelForm):
    national_id = forms.FileInput()
    title = forms.Select()
    first_name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    gender = forms.Select()
    marital_status = forms.Select()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    national_id_no = forms.CharField(max_length=12)
    email = forms.EmailField()
    mobile_number = forms.IntegerField()
    
    class Meta:
        model = Applicant
        fields = ['national_id','title','first_name','surname'\
                 ,'gender','marital_status','dob',\
                     'national_id_no',\
                         'email','mobile_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['national_id'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['surname'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['gender'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['marital_status'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['dob'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['national_id_no'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['mobile_number'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        
class ApplicationForm2(forms.ModelForm):
    resident = forms.Select()
    address = forms.CharField(max_length=100)
    street_name= forms.CharField(max_length=100)
    town = forms.CharField(max_length=100)

    class Meta:
        model = AddressDetails
        fields = ['resident','address','street_name','town']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resident'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['street_name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['town'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        
class ApplicationForm3(forms.ModelForm):
    title = forms.Select()
    first_name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    national_id_no = forms.CharField(max_length=12)
    relationship = forms.CharField(max_length=100)
    contact_number = forms.IntegerField()
    

    class Meta:
        model = NextOfKinDetails
        fields = ['title','first_name','surname','national_id_no','relationship','contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['surname'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['national_id_no'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['relationship'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['contact_number'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})

class ApplicationForm4(forms.ModelForm):
    
    employer_name = forms.CharField(max_length=100)
    employee_number = forms.CharField(max_length=100)
    profession = forms.CharField(max_length=100)

    class Meta:
        model = EmploymentDetails
        fields = ['employer_name','employee_number','profession']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employer_name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['employee_number'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['profession'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        
class ApplicationForm5(forms.ModelForm):
    bank_name = forms.CharField(max_length=100)
    branch_name = forms.CharField(max_length=100)
    account_no = forms.IntegerField()

    class Meta:
        model = BankDetails
        fields = ['bank_name','branch_name','account_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bank_name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['branch_name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['account_no'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        
class LoanForm(forms.ModelForm):
    loan_type = forms.Select()
    product = forms.SelectMultiple()
    disbursement_option = forms.Select()
    existing_loan_amount= forms.Select()
    loan_tenure = forms.Select()

    class Meta:
        model = LoanDetails
        fields = ['loan_type','product','disbursement_option','existing_loan_amount','loan_tenure']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan_type'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['product'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['disbursement_option'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['existing_loan_amount'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['loan_tenure'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        
        

        
