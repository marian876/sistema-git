from django.contrib.auth.models import Group

class GroupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        grupo = None
        nombre_grupo = None
        if user.is_authenticated:
            grupo = Group.objects.filter(user=user).first()
            if grupo:
                nombre_grupo = grupo.name  # Asegúrate de que 'name' es el atributo correcto para el nombre del grupo
        request.grupo = grupo
        request.nombre_grupo = nombre_grupo

        response = self.get_response(request)

        return response
