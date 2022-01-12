
from django.db import models
from django.db.models.expressions import RowRange

class Event(models.Model):
    activity=models.CharField(max_length=300,null=False),
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=30)

class ContactUs(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Phone_number=models.IntegerField()
    Email_address=models.EmailField()
    message=models.TextField()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

    def save_date(self):
        self.save()
        
# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'

    def save_date(self):
        self.save()
class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'

    def save_date(self):
        self.save()

class M_Pesa(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        return self.first_name

    def save_date(self):
        self.save()

class  pay(models.Model):
    phone_number=models.IntegerField() 
    pay=models.DecimalField(max_digits=6, decimal_places=2)
