from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def medical(request):
    return render(request,'main/medical_services.html')

def education(request):
    return render(request,'main/education_services.html')