from django.db import models
from django.contrib.auth import get_user_model

class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sucursal = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to='unirpdf/')
