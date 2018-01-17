# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Alumno, Asignatura, Matricula
# Create your views here.

def home(request):
    context = {}
    context['alumnos'] = Alumno.objects.all()
    context['asignaturas'] = Asignatura.objects.all()
    return render(request, 'home.html', context)

def alumno(request, pk):
    context = {}
    context['alumno'] = Alumno.objects.get(pk=pk)

    return render(request, 'alumno.html', context)

def asignatura(request, pk):
    context = {}
    context['asignatura'] = Asignatura.objects.get(pk=pk)

    context['aplazados'] = 0
    context['total'] = context['asignatura'].alumnos.count()
    for alumno in context['asignatura'].alumnos.all():
        if alumno.promedio()<6:
            context['aplazados']+=1
    context['porcentaje'] = context['aplazados'] * 100 / context['total']
    return render(request, 'asignatura.html', context)
