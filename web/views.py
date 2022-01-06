from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from .forms import Contact_Form

def index(request):
    return render(request,'main/index.html')

def medical(request):
    return render(request,'main/medical_services.html')

def education(request):
    return render(request,'main/education_services.html')

def donate(request):
    return render(request,'main/donate.html')

def specialist(request):
    return render(request,'main/specialist.html')

def outpatient(request):
    return render(request,'main/outpatient.html')

def inpatient(request):
    return render(request,'main/inpatient.html')

def contactus(request):
    form=Contact_Form()
    return render(request,'main/contactus.html',{'Contact_Form':Contact_Form})