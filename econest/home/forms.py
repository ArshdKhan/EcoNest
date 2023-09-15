from django import forms
from .models import Neighbourhood_Info

class Neighbourhood(forms.ModelForm):
    class meta:
        model=Neighbourhood_Info
        fields=['neighbourhood','average_rent']
