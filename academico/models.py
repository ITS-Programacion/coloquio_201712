# -*- coding: utf-8 -*-
##NO LE ANDA LA TILDE A MI BRACKETS...

from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
class Alumno(models.Model):
    '''
    Un alumno tiene los datos basicos
    '''
    nombre = models.CharField(_('Nombre'), max_length=128)
    apellido = models.CharField(_('Apellido'), max_length=128)
    dni = models.PositiveIntegerField(_('DNI'))

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Asignatura(models.Model):
    '''
    Una asignatura tiene los datos basicos
    '''
    title = models.CharField(_('Título'), max_length=128)
    docente = models.CharField(_('Docente'), max_length=128)
    carga_horaria = models.PositiveIntegerField(_('Carga Horaria'))

    def __str__(self):
        return '{}'.format(self.title)

class Matricula(models.Model):
    '''
    Relaciona al alumno con la asignatura,
    y me va a permitir relacionarlo con las notas
    '''
    alumno = models.ForeignKey(Alumno, related_name='asignaturas')
    asignatura = models.ForeignKey(Asignatura, related_name='alumnos')

    def promedio(self):
        suma = 0
        total = self.notas.count()
        if total <= 0:
            return 0
        for nota in self.notas.all():
            suma += nota.valor
        return float(suma)/total

    def __str__(self):
        return '{}: {} = {}'.format(self.asignatura, self.alumno, self.promedio())


class Nota(models.Model):
    '''
    Relaciona al alumno con la asignatura,
    y me va a permitir relacionarlo con las notas
    '''
    matricula = models.ForeignKey(Matricula, related_name='notas')
    valor = models.PositiveIntegerField(_('Valor'))

    def __str__(self):
        return '{}: {} = {}'.format(self.matricula.asignatura, self.matricula.alumno, self.valor)
