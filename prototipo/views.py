from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Paciente, Difunto, Doctor, Hospital
from .forms import PacienteForm, DifuntoForm, DoctorForm, HospitalForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Formulario no válido.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'index.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')

def paciente(request):
    agregar_paciente = None
    if request.method == 'POST':
        if 'id_update' in request.POST:
            paciente = get_object_or_404(Paciente, id=request.POST['id_update'])
            form = PacienteForm(request.POST, instance=paciente)
        else:
            form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente')
    elif 'id_update' in request.GET:
        agregar_paciente = get_object_or_404(Paciente, id=request.GET.get('id_update'))
        form = PacienteForm(instance=agregar_paciente)
    
    elif 'id_delete' in request.GET:
        eliminar_paciente = get_object_or_404(Paciente, id=request.GET.get('id_delete'))
        eliminar_paciente.delete()
        return redirect('paciente')
    else:
        form = PacienteForm()
    
    pacientes = Paciente.objects.all()

    context = {
        'form': form,
        'pacientes': pacientes,
        'agregar_paciente': agregar_paciente,
    }
        
    return render(request, 'paciente.html', context)

def difunto(request):
    agregar_difunto = None
    if request.method == 'POST':
        if 'id_update' in request.POST:
            difunto = get_object_or_404(Difunto, id=request.POST['id_update'])
            form = DifuntoForm(request.POST, instance=difunto)
        else:
            form = DifuntoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('difunto')
    elif 'id_update' in request.GET:
        agregar_difunto = get_object_or_404(Difunto, id=request.GET.get('id_update'))
        form = DifuntoForm(instance=agregar_difunto)
    
    elif 'id_delete' in request.GET:
        eliminar_difunto = get_object_or_404(Difunto, id=request.GET.get('id_delete'))
        eliminar_difunto.delete()
        return redirect('difunto')
    else:
        form = DifuntoForm()
    
    difuntos = Difunto.objects.all()

    context = {
        'form': form,
        'difuntos': difuntos,
        'agregar_difunto': agregar_difunto,
    }
        
    return render(request, 'difunto.html', context)

def hospital(request):
    agregar_hospital = None
    if request.method == 'POST':
        if 'id_update' in request.POST:
            hospital = get_object_or_404(Hospital, id=request.POST['id_update'])
            form = HospitalForm(request.POST, instance=hospital)
        else:
            form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital')
    elif 'id_update' in request.GET:
        agregar_hospital = get_object_or_404(Hospital, id=request.GET.get('id_update'))
        form = HospitalForm(instance=agregar_hospital)
    
    elif 'id_delete' in request.GET:
        eliminar_hospital = get_object_or_404(Hospital, id=request.GET.get('id_delete'))
        eliminar_hospital.delete()
        return redirect('hospital')
    else:
        form = HospitalForm()
    
    hospitales = Hospital.objects.all()

    context = {
        'form': form,
        'hospital': hospitales,
        'agregar_hospital': agregar_hospital,
    }
        
    return render(request, 'hospital.html', context)

def doctor(request):
    agregar_doctor = None
    if request.method == 'POST':
        if 'id_update' in request.POST:
            doctor = get_object_or_404(Doctor, id=request.POST['id_update'])
            form = DoctorForm(request.POST, instance=doctor)
        else:
            form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor')
    elif 'id_update' in request.GET:
        agregar_doctor = get_object_or_404(Doctor, id=request.GET.get('id_update'))
        form = DoctorForm(instance=agregar_doctor)
    
    elif 'id_delete' in request.GET:
        eliminar_doctor = get_object_or_404(Doctor, id=request.GET.get('id_delete'))
        eliminar_doctor.delete()
        return redirect('doctor')
    else:
        form = DoctorForm()
    
    doctores = Doctor.objects.all()

    context = {
        'form': form,
        'doctores': doctores,
        'agregar_doctor': agregar_doctor,
    }
        
    return render(request, 'doctor.html', context)