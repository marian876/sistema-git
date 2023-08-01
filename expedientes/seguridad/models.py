from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', verbose_name="Usuario")
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Apellido')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ciudad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nro Celular')
    image = models.ImageField(default='seguridad/imagen/usuario_defecto.png', upload_to='seguridad/imagen/', verbose_name='Imagen de perfil', null=True, blank=True)
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)
