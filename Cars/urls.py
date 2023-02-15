from django.urls import path 
from .import views 

urlpatterns = [
    path("AddCar",views.AddCar,name="AddCar"),
    path("CarDetails",views.CarDetails,name="CarDetails"),
    path("CarListing",views.CarListing,name="CarListing"),
    path("CarSingleView/<int:pk>",views.CarSingleView,name="CarSingleView"),
    path("DeleteCar/<int:pk>",views.DeleteCar,name="DeleteCar"),
    path("MovieToCarrage/<int:pk>",views.MovieToCarrage,name="MovieToCarrage"),
    path("ListToRent/<int:pk>",views.ListToRent,name="ListToRent"),
    
]
