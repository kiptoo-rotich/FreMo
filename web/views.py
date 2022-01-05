from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404

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