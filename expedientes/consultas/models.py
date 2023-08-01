from typing import Any, Dict, Tuple
from django.db import models

class Expediente(models.Model):
    id_expediente = models.IntegerField(primary_key=True, verbose_name="ID Expediente")
    id_proceso = models.CharField(max_length=100, verbose_name="ID Proceso")
    indice_01 = models.CharField(max_length=254, verbose_name="Nombre")
    indice_02 = models.CharField(max_length=254, verbose_name="Índice 2", blank=True)
    indice_03 = models.CharField(max_length=254, verbose_name="Índice 3", blank=True)
    indice_04 = models.CharField(max_length=254, verbose_name="Índice 4", blank=True)
    indice_05 = models.CharField(max_length=254, verbose_name="Índice 5", blank=True)
    ruta_original = models.CharField(max_length=254, verbose_name="Ruta Original", blank=True)
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación", blank=True)
    estado = models.CharField(max_length=50, verbose_name="Estado", default='Activo', blank=True)
    paginas = models.IntegerField(verbose_name="Páginas", null=True, blank=True)
    imagen = models.ImageField(upload_to='expedientes/imagen/', verbose_name="Imagen", null=True, blank=True)
    
    def __str__(self):
        fila = "ID Expediente: " + str(self.id_expediente) + " - " + "Estado: " + self.estado
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
