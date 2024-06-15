from django import forms
from .models import Safar

class DeliveryRequestForm(forms.ModelForm):
    class Meta:
        model = Safar
        fields = ['origin_location_lat', 'origin_location_lon','destination_location_lat','destination_location_lon']
