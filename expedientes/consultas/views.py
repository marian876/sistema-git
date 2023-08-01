from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Expediente
from .forms import ExpedienteForm
from django.contrib.auth.models import Group

def inicio(request):
    return render(request,'paginas/inicio.html', {'pestaña_activa': 'inicio'})


def ayuda(request):
    return render(request,'paginas/ayuda.html', {'pestaña_activa': 'ayuda'})

def consulta(request):
    consulta = Expediente.objects.all()
    field_names = {
        'id_expediente': Expediente._meta.get_field('id_expediente').verbose_name,
        'indice_01': Expediente._meta.get_field('indice_01').verbose_name,
        'imagen': Expediente._meta.get_field('imagen').verbose_name,
        'estado': Expediente._meta.get_field('estado').verbose_name,
    }
    return render(request, 'expedientes/consulta.html', {'expedientes': consulta, 'field_names': field_names, 'pestaña_activa': 'consulta'})

def gestion(request):
    gestion=Expediente.objects.all()
    field_names = {
        'id_expediente': Expediente._meta.get_field('id_expediente').verbose_name,
        'imagen': Expediente._meta.get_field('imagen').verbose_name,
        'id_proceso': Expediente._meta.get_field('id_proceso').verbose_name,
        'indice_01': Expediente._meta.get_field('indice_01').verbose_name,
        'indice_02': Expediente._meta.get_field('indice_02').verbose_name,
        'indice_03': Expediente._meta.get_field('indice_03').verbose_name,
        'indice_04': Expediente._meta.get_field('indice_04').verbose_name,
        'indice_05': Expediente._meta.get_field('indice_05').verbose_name,
        'ruta_original': Expediente._meta.get_field('ruta_original').verbose_name,
        'ubicacion': Expediente._meta.get_field('ubicacion').verbose_name,
        'estado': Expediente._meta.get_field('estado').verbose_name,
        'paginas': Expediente._meta.get_field('paginas').verbose_name,
    }
    return render(request, 'expedientes/gestion.html', {'expedientes':gestion, 'field_names': field_names, 'pestaña_activa': 'gestion'})

def crear(request):
    formulario=ExpedienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect(reverse('gestion'))
    return render(request,'expedientes/crear.html',{'formulario':formulario, 'pestaña_activa': 'crear'})

def editar(request,id_expediente):
    expediente=Expediente.objects.get(id_expediente=id_expediente)
    formulario=ExpedienteForm(request.POST or None, request.FILES or None, instance=expediente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return HttpResponseRedirect(reverse('gestion'))
    return render(request,'expedientes/editar.html',{'formulario':formulario, 'pestaña_activa': 'editar'})

def eliminar(request,id_expediente):
    expediente=Expediente.objects.get(id_expediente=id_expediente)
    expediente.delete()
    return HttpResponseRedirect(reverse('gestion'))

def buscar_consultar(request):
    busqueda=request.POST.get("buscar")
    expedientes = None
    busqueda_realizada = False

    if busqueda:
        busqueda_realizada = True
        expedientes = Expediente.objects.filter(
            Q(id_expediente__icontains=busqueda) |
            Q(indice_01__icontains=busqueda)
        ).distinct()

    return render(request, 'expedientes/consulta.html', {'expedientes': expedientes, 'busqueda_realizada': busqueda_realizada, 'pestaña_activa': 'consulta'})

def buscar_gestion(request):
    busqueda=request.POST.get("buscar")
    expedientes=Expediente.objects.all()

    if busqueda:
        expedientes = Expediente.objects.filter(
            Q(id_expediente__icontains=busqueda) |
            Q(id_proceso__icontains=busqueda) |
            Q(indice_01__icontains=busqueda) |
            Q(indice_02__icontains=busqueda) |
            Q(indice_03__icontains=busqueda) |
            Q(indice_04__icontains=busqueda) |
            Q(indice_05__icontains=busqueda) |
            Q(estado=busqueda) 

        ).distinct()

    return render(request, 'expedientes/gestion.html', {'expedientes': expedientes, 'busqueda_realizada': expedientes, 'pestaña_activa': 'gestion'})

def movimiento(request):
    return render(request,'expedientes/movimiento.html', {'pestaña_activa': 'movimiento'})

