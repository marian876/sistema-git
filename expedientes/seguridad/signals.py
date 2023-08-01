from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_usuarios_group(sender, instance, created, **kwargs):
    if created:
        try:
            grupo1 = Group.objects.get(name='Visor')
        except Group.DoesNotExist:
            grupo1 = Group.objects.create(name='Visor')
            grupo2 = Group.objects.create(name='Gestor')
            grupo3 = Group.objects.create(name='Administrador')
        instance.user.groups.add(grupo1)