from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section': 'dashboard'}
    )

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
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