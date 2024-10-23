from django.contrib import admin
from .models import Paciente, Difunto, Hospital, Doctor, Especialidad

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Difunto)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Especialidad)
