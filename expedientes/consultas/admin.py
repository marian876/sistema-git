from django.contrib import admin
from .models import Expediente

class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ('id_expediente', 'id_proceso', 'indice_01', 'indice_02', 'indice_03', 'indice_04', 'indice_05', 'ruta_original', 'ubicacion', 'estado', 'paginas', 'imagen')
    search_fields = ('id_expediente', 'id_proceso', 'estado')
    list_filter = ('estado',)

admin.site.register(Expediente, ExpedienteAdmin)
