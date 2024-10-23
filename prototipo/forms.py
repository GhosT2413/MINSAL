from django import forms
from .models import Paciente, Difunto, Doctor, Hospital

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['tipo', 'nombre', 'cantidad', 'caducidad', 'descripcion']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'caducidad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DifuntoForm(forms.ModelForm):
    class Meta:
        model = Difunto
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'fecha_fallecimiento', 'hora_muerte', 'genero', 'direccion', 'telefono', 'email', 'causa_muerte']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fallecimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_muerte': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'causa_muerte': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento', 'genero', 'direccion', 'telefono', 'email', 'especialidad']
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
        }

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital', 'direccion', 'jefe_hospital', 'telefono']
        widgets = {
            'hospital': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'jefe_hospital': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
