from django import forms

class RepuestosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required= True)
    marca = forms.CharField(max_length=50, required= True)
    precio = forms.IntegerField(required= True)
    cantidad =forms.IntegerField(required= True)

class MaquinaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required= True)
    marca = forms.CharField(max_length=50, required= True)
    area = forms.CharField(max_length=50, required= True)

class ProveedoresForm(forms.Form):
    nombre = forms.CharField(max_length=50, required= True)
    direccion = forms.CharField(max_length=50, required= True)
    fono = forms.IntegerField()
    email = forms.EmailField()
