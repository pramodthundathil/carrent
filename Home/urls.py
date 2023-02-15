from django.urls import path 
from .import views 
urlpatterns = [
     path("",views.Index,name="Index"),
     path("ManagerHome",views.ManagerHome,name="ManagerHome"),
     path("SignIn",views.SignIn,name="SignIn"),
     path("SignUp",views.SignUp,name="SignUp"),
     path("SignOut",views.SignOut,name="SignOut"),
     
]
