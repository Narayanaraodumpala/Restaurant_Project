from django import forms
from restarent_app.models import *


class RestaurentForm(forms.ModelForm):
    class Meta:
        model=RestaurentModel
        fields ="__all__"

class Addfoodform(forms.ModelForm):
    class Meta:
        model=AddFoodModel
        fields="__all__"