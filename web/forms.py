from django.db import models
from django.db.models import fields
from django.db.models.expressions import RowRange
from .models import ContactUs,M_Pesa
from django import forms
from django.core.validators import RegexValidator


def My_TextField_Validator(self):
    return RegexValidator(r'^[-a-zA-Z0-9. ]+$',
    'Valid Input: Alphanumeric characters, dash, dot, space')

class Contact_Form(forms.ModelForm):
    First_name = forms.CharField(max_length=50, min_length=4, required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'First name'}))
    
    Last_name = forms.CharField(max_length=50, min_length=4, required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Last name'}))
    Email_address = forms.CharField(max_length=50, min_length=4, required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'johndoe@gmail.com'}))     
    Phone_number = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Phone number'}))   
    message = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.Textarea(attrs={'class': 'form-control', 
                           'placeholder': 'My message is ...'})) 
    class Meta:
        model=ContactUs
        fields='__all__'


class Payment_Form(forms.ModelForm):   
    phone_number = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Phone number'}))   

    amount = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Amount'})) 

    description = forms.CharField(required=True,
                           help_text='', label='',
                           validators=[My_TextField_Validator],
                           widget=forms.Textarea(attrs={'class': 'form-control', 
                           'placeholder': 'This payments is ...'})) 
    class Meta:
        model=M_Pesa
        fields=['phone_number','amount','description']
