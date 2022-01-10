from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from .forms import Contact_Form,Payment_Form

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

def ultrasound(request):
    return render(request,'main/ultra_sound.html')

def laboratory(request):
    return render(request,'main/laboratory.html')

def pharmacy(request):
    return render(request,'main/pharmacy.html')

def aboutus(request):
    return render(request,'main/aboutus.html')

def counselling(request):
    return render(request,'main/counselling.html')

def nutrition(request):
    return render(request,'main/nutrition.html')

def school(request):
    return render(request,'main/school.html')

def book(request):
    form=Contact_Form()
    return render(request,'main/book.html',{'Contact_Form':form})

def pay(request):
    form=Payment_Form()
    return render(request,'main/payments.html',{'Payment_Form':form})

def donate(request):
    form=Payment_Form()
    return render(request,'main/donation.html',{'Payment_Form':form})