from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from seguridad.views import CustomSignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('consultas.urls')),
    path('seguridad/', include('seguridad.urls')),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/', include('allauth.urls')),
    path('unirpdf/', include('unirpdf.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
