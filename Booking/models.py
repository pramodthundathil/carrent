from django.db import models
from Cars.models import Cars
from django.contrib.auth.models import User

class Booking(models.Model):
    Car = models.ForeignKey(Cars,on_delete=models.CASCADE,null=True,blank=True)
    Customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    StartDate = models.DateField(auto_now_add=False)
    EndDate = models.DateField(auto_now_add=False)
    numberofdays = models.CharField(max_length=12,null=True)
    amount = models.IntegerField(null=True)
    paymentstatus = models.BooleanField(default=False)
    BookDate = models.DateField(auto_now_add=True)
