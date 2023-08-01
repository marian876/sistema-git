from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('consulta',views.consulta, name='consulta'),
    path('consulta/buscar', views.buscar_consultar, name='buscar_consultar'),
    path('gestion',views.gestion, name='gestion'),
    path('gestion/buscar', views.buscar_gestion, name='buscar_gestion'),
    path('gestion/crear',views.crear, name='crear'),
    path('gestion/editar/<int:id_expediente>',views.editar, name='editar'),
    path('gestion/eliminar/<int:id_expediente>',views.eliminar, name='eliminar'),
    path('movimiento',views.movimiento, name='movimiento'),

    path('ayuda',views.ayuda, name='ayuda'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)