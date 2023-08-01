from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser, Profile


class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario registrado con esta dirección de correo electrónico.")
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'address', 'location', 'telephone', 'first_name', 'last_name']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # o CustomUser, si eso es lo que estás usando
        fields = ['first_name', 'last_name']  # o los campos que quieras permitir editar

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'address', 'location', 'telephone', 'first_name', 'last_name']  # o los campos que quieras permitir editar
