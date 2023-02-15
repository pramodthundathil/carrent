from django.forms import ModelForm,TextInput
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["StartDate","EndDate"]
        
        widgets = {
            "StartDate":TextInput(attrs={"type":"date"}),
            "EndDate":TextInput(attrs={"type":"date"}),
            
        }