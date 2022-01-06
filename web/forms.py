from django.db import models
from django.db.models import fields
from .models import ContactUs
from django import forms

class Contact_Form(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'
