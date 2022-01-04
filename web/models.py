from django.db import models

class Event(models.Model):
    activity=models.CharField(max_length=300,null=False),
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=30)

class M_Pesa(models.Model):
    phone_number=models.IntegerField()
    amount=models.IntegerField()