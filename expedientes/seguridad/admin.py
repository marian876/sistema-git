from django.contrib import admin
from .models import Profile, CustomUser

# PROFILE DETALLADO
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'address', 'location', 'telephone', 'user_group','image')
    search_fields =('location', 'user__username', 'user__groups__name')
    list_filter = ('user__groups', 'location')

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # ajusta estos campos a tus necesidades
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)  # modificado para incluir CustomUserAdmin
