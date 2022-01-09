
from django.db import models
from django.db.models.expressions import RowRange

class Event(models.Model):
    activity=models.CharField(max_length=300,null=False),
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=30)

class M_Pesa(models.Model):
    phone_number=models.IntegerField()
    amount=models.IntegerField()
    description=models.CharField(max_length=300)

class ContactUs(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Phone_number=models.IntegerField()
    Email_address=models.EmailField()
    message=models.TextField()
