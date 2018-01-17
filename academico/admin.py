# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Matricula)
admin.site.register(Nota)
