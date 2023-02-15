from django.db import models
from django.contrib.auth.models import User


class Cars(models.Model):
    
    options = (
        ("Hatchback", "Hatchback"),
        ("Sedan","Sedan"), 
        ("SUV", "SUV"),
        ("MUV","MUV"),
        ("Coupe","Coupe"),
        ( "Convertible","Convertible"),
        ("Pickup Truck","Convertible")
    )
    option2 = (
    ("Listed For Rentel","Listed For Rentel"),
    ("Not Listed For Rentel","Not Listed For Rentel"),
    ("In Garrage","In Garrage"),
    ("On Rentel","On Rentel")
    )
    
    Manager = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Car_Name = models.CharField(max_length=255)
    Car_Brand = models.CharField(max_length=255)
    Car_Category = models.CharField(max_length=255,choices=options)
    Plate_Number = models.CharField(max_length=255)
    Model_Year = models.DateField(auto_now_add=False)
    Car_Image = models.ImageField(upload_to="car_image")
    Kilomeaters = models.CharField(max_length=12,null=True)
    Rent = models.CharField(max_length=12)
    Car_Status = models.CharField(max_length=255,choices=option2,null=True)
    
