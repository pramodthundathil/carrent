from django.urls import path 
from .import views

urlpatterns = [
    path("CarView/<int:pk>",views.CarView,name="CarView"),
    path("Mybookings",views.Mybookings,name="Mybookings"),
    path("DeleteBooking/<int:pk>",views.DeleteBooking,name="DeleteBooking"),
    path("MakePayment/<int:pk>",views.MakePayment,name="MakePayment"),
    path("MakePayment/paymenthandler/",views.paymenthandler,name="MakePayment/paymenthandler"),
    path("BookingManagerView",views.BookingManagerView,name="BookingManagerView"),
    path("DeleteBookingAdmin/<int:pk>",views.DeleteBookingAdmin,name="DeleteBookingAdmin")
]
