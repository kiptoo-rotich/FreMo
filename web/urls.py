from . import views
from django.urls import path


urlpatterns=[    
    path('', views.index,name='Home'),
    path('medical_services/',views.medical,name="Medical"),
    path('education_services/',views.education,name="Education"),
    path('donate_money/',views.donate,name="Donations"),
    path('specialist_clinic/',views.specialist,name="specialist"),
    path('outpatient_clinic/',views.outpatient,name="outpatient"),
    path('inpatient_clinic/',views.inpatient,name="inpatient")
]