from django.shortcuts import render,redirect
from .forms import UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
from Cars.models import Cars
from Booking.models import Booking
# Create your views here.

@admin_only
def Index(request):
    cars = Cars.objects.filter(Car_Status = "Listed For Rentel")
    
    context = {
        "cars":cars
    }
    return render(request,"index.html",context)

@login_required(login_url="SignIn")
def ManagerHome(request):
    
    context = {
        "totalcars":Cars.objects.all().count(),
        "Garrage":Cars.objects.filter(Car_Status = "In Garrage").count(),
        "bookings":Booking.objects.all().count()
    }
    return render(request,"managerhome.html",context)

def SignIn(request):
    
    if request.method == 'POST' :
        username = request.POST['uname']
        password = request.POST['pswd']
        
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        else:
            messages.info(request,"Username or password Incorrect")
            return redirect('SignIn')
        
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"User Created")
            return redirect('SignIn')
    context = {
        "form":form
    }
        
    return render(request,"register.html",context)

def SignOut(request):
    logout(request)
    return redirect('Index')
