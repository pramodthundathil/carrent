from django.forms import ModelForm,TextInput
from .models import Cars

class CarAddForm(ModelForm):
    class Meta:
        model = Cars
        fields = ["Car_Name","Car_Brand","Car_Category","Plate_Number","Model_Year","Kilomeaters","Rent","Car_Image"]
        widgets = {
            "Model_Year":TextInput(attrs={"type":"date"}),
            "Plate_Number":TextInput(attrs={"placeholder":"eg: KL-43-E-7479"})
        }