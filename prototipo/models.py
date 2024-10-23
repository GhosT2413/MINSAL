from django.db import models
from django.core.validators import RegexValidator



class Genero(models.TextChoices):
    FEMENINO = 'F', 'Femenino'
    MASCULINO = 'M', 'Masculino'


class Hospital(models.Model):
    hospital = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    jefe_hospital = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.hospital

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.especialidad
    
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    numero = models.IntegerField()  # Corregido para ser un campo de modelo
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paciente(models.Model):
    tipo = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    caducidad = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Difunto(models.Model): 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField()
    hora_muerte = models.TimeField(default=1)
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    causa_muerte = models.TextField()
    doctor_cargo = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)  # Permitir nulos
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
