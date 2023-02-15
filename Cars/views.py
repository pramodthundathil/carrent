from django.shortcuts import render,redirect
from .forms import CarAddForm
from django.contrib import messages
from .models import Cars
from django.contrib.auth.decorators import login_required


@login_required(login_url="SignIn")
def AddCar(request):
    form = CarAddForm()
    if request.method == "POST":
        form = CarAddForm(request.POST,request.FILES)
        if form.is_valid():
            car = form.save()
            car.Manager = request.user
            car.Car_Status = "In Garrage"
            car.save()
            messages.info(request,"Car details Saved")
            return redirect('AddCar')
    
    context = {
        "form":form
    }
    return render(request,"addcar.html",context)

@login_required(login_url="SignIn")
def CarDetails(request):
    cars = Cars.objects.all()
    context = {
        "cars":cars
    }
    return render(request,"cardetails.html",context)


@login_required(login_url="SignIn")
def CarListing(request):
    cars = Cars.objects.filter(Car_Status = "Listed For Rentel")
    
    context = {
        "cars":cars
    }
    return render(request,"car.html",context)

@login_required(login_url="SignIn")
def CarSingleView(request,pk):
    car = Cars.objects.filter(id = pk)
    if request.method == "POST":
        cars = Cars.objects.get(id = pk)
        cars.Car_Name = request.POST["carname"]
        cars.Car_Brand = request.POST['brand']
        cars.Car_Category = request.POST["catego"]
        cars.Plate_Number = request.POST["pnum"]
        cars.Model_Year = request.POST["year"]
        cars.Car_Image.delete()
        cars.Car_Image = request.FILES['img']
        cars.Kilomeaters = request.POST["klm"]
        cars.Rent = request.POST["rent"]
        cars.save()
        return redirect('CarSingleView',pk=pk)
        
    context = {
        "car":car
    }
    return render(request,"carsingleview.html",context)

@login_required(login_url="SignIn")
def DeleteCar(request,pk):
    car = Cars.objects.get(id = pk)
    car.Car_Image.delete()
    car.delete()
    messages.info(request,"Car deleted")
    return redirect("CarDetails")

@login_required(login_url="SignIn")
def MovieToCarrage(request,pk):
    car = Cars.objects.get(id = pk)
    car.Car_Status = "In Garrage"
    car.save()
    messages.info(request,"Value Changed")
    return redirect("CarSingleView",pk = pk)

@login_required(login_url="SignIn")
def ListToRent(request,pk):
    car = Cars.objects.get(id = pk)
    car.Car_Status = "Listed For Rentel"
    car.save()
    messages.info(request,"Value Changed")
    return redirect("CarSingleView",pk = pk)