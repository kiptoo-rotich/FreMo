from . import views
from django.urls import path


urlpatterns=[    
    path('', views.index,name='Home'),
    path('medical_services/',views.medical,name="Medical"),
    path('education_services/',views.education,name="Education"),
    path('donate_money/',views.donate,name="Donations"),
    path('specialist_clinic/',views.specialist,name="specialist"),
    path('outpatient_clinic/',views.outpatient,name="outpatient"),
    path('inpatient_clinic/',views.inpatient,name="inpatient"),
    path('contact_us/',views.book,name="contact_us"),
    path('ultra_sound/',views.ultrasound,name="ultrasound"),
    path('laboratory/',views.laboratory,name="laboratory"),
    path('pharmacy/',views.pharmacy,name="pharmacy"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('counselling/',views.counselling,name="counselling"),
    path('nutrition/',views.nutrition,name="nutrition"),
    path('lipa_na_mpesa_online/',views.lipa_na_mpesa_online,name="lipa_na_mpesa_online"),
    path('lipa_na_mpesa_donate/',views.lipa_na_mpesa_donation,name="lipa_na_mpesa_donation"),
    path('school/',views.school,name="school"),
    path('volunteer/',views.volunteer,name="volunteer"),
    
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
   
]