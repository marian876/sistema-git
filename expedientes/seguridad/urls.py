from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('perfil',views.profile, name='perfil'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)