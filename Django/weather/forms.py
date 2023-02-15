from django import forms


class CityForm(forms.Form):
    cityName = forms.CharField(label="City Name", max_length=200)
