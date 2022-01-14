from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Departamento, Empleado, Habilidad

# Create your views here.

from django.http import HttpResponse

# Devuelve el listado de empresas
# def index(request):
#    departamentos = Departamento.objects.order_by('nombre')
#    context = {'titulo_pagina' : 'Listado de Departamentos', 'lista_departamentos' : departamentos}
#    return render(request, 'departamentos.html', context)

class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamentos.html'
    queryset = Departamento.objects.order_by('nombre')
    context_object_name ='lista_departamentos'

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de departamentos'
        return context

# Devuelve los datos de un departamento por ID
def departamento(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    return HttpResponse(departamento)    

def empleados(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    output = '////'.join(str(empleado) for empleado in departamento.empleado_set.all())
    return HttpResponse(output)

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        return context

# def empleado(request, empleado_id):
#    empleado = Empleado.objects.get(pk=empleado_id)
#    context = {'titulo_pagina' : 'Detalles del empleado', 'empleado' : empleado}
#    return render(request, 'empleado.html', context)

def habilidad(request, habilidad_id):
    empleado = Habilidad.objects.get(pk=habilidad_id)
    return HttpResponse(empleado)