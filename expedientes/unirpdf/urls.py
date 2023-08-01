from django.urls import path
from . import views
from .views import cargar_pdfs, verificar_pdf, consultar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cargar_pdf/', views.cargar_pdfs, name='cargar_pdf'),
    path('verificar/', views.verificar_pdf, name='verificar_pdf'),
    path('verificar/cancelar/<str:path>/', views.cancelar_pdf, name='cancelar_pdf'),
    path('consultar/', consultar, name='consultar_pdf'), 
    path('consultar/buscar/', views.buscar_reportes, name='buscar_reportes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

