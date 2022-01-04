from . import views
from django.urls import path


urlpatterns=[    
    path('', views.index,name='Home'),
    path('medical_services/',views.medical,name="Medical"),
    path('education_services/',views.education,name="Education"),
    path('donate_money/',views.donate,name="Donations")
]