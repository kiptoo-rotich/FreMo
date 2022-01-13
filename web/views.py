import json

import requests
from django.http import HttpResponse, JsonResponse
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests.auth import HTTPBasicAuth

from .forms import Contact_Form, Payment_Form
from .m_pesa_credentials import LipanaMpesaPpassword, MpesaAccessToken
from .models import M_Pesa, pay
from .m_pesa_credentials import LipanaMpesaPpassword, MpesaAccessToken


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

def volunteer(request):
    return render(request,'main/volunteer.html')

def getAccessToken(request):
    return HttpResponse("Hello, world")


def getAccessToken(request):
    consumer_key = 'cWYTdP54T3Bg8snmp7CUm9FHCy4lXtfX'
    consumer_secret = 'dWUXM78C19L9Vn35'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    if request.method=="POST":
        transaction_number=request.POST.get('phone_number')
        cell= str(254)+str(int(transaction_number))
        remiting_number=int(cell)
        amount=request.POST.get('pay')

        form= Payment_Form(request.POST)
        if form.is_valid():
            amount= form.cleaned_data.get("amount")
            description= form.cleaned_data.get("description")
            phone_number= form.cleaned_data.get("phone_number")
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": int(amount),
                "PartyA": remiting_number, 
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": remiting_number, 
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Kiptoo",
                "TransactionDesc": "Testing stk push"
            }

            response = requests.post(api_url, json=request, headers=headers)
            return HttpResponse(f'Kindly check your phone {remiting_number} and enter mpesa pin to succesfully pay fare')
    else:
        form= Payment_Form()
        return render(request,'main/payments.html',{'Payment_Form':form})


def lipa_na_mpesa_donation(request):
    if request.method=="POST":
        transaction_number=request.POST.get('phone_number')
        cell= str(254)+str(int(transaction_number))
        remiting_number=int(cell)
        amount=request.POST.get('pay')

        form= Payment_Form(request.POST)
        if form.is_valid():
            amount= form.cleaned_data.get("amount")
            description= form.cleaned_data.get("description")
            phone_number= form.cleaned_data.get("phone_number")
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": int(amount),
                "PartyA": remiting_number, 
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": remiting_number, 
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Kiptoo",
                "TransactionDesc": "Testing stk push"
            }

            response = requests.post(api_url, json=request, headers=headers)
            return HttpResponse(f'Kindly check your phone {remiting_number} and enter mpesa pin to succesfully pay fare')
    else:
        form= Payment_Form()
        return render(request,'main/donation.html',{'Payment_Form':form})


