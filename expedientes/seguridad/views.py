from django.shortcuts import render, redirect
from .models import Profile
from seguridad import views as seguridad_views
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserEditForm, ProfileEditForm


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'seguridad/perfil.html', {'user_form': user_form, 'profile_form': profile_form})


class CustomSignupView(SignupView):
    form_class = CustomSignupForm