import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):
    user_profile = Profile.objects.filter(user_id=request.user.id).first()
    return render(
        request,
        'account/dashboard.html',
        {
            'section': 'dashboard',
            'user_profile': user_profile
        }
    )

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return render(
                request,
                'registration/register_done.html',
                {'form': user}
            )
    else:
        form = UserRegistrationForm()
    return render(
        request,
        'registration/register.html',
        {'form': form}
    )

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        old_profile = Profile.objects.filter(id=request.user.profile.id).first()
        if old_profile.photo and os.path.exists(old_profile.photo.path):
            os.remove(old_profile.photo.path)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )