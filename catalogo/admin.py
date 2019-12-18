from django.contrib import admin
from .models import Cliente, Orden, tecnico

admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(tecnico)