from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . import forms


app_name = "account"

urlpatterns = [
    path(
        "login/", 
        auth_views.LoginView.as_view(
            authentication_form=forms.LoginForm
        ), 
        name="login"
    ),
    path(
        "logout/", 
        auth_views.LogoutView.as_view(), 
        name="logout"
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            form_class=forms.CustomPasswordChangeForm,
            template_name="registration/password_change_form.html",
            success_url=reverse_lazy("account:password_change_done"),
        ),
        name='password_change'
    ),
    path(
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html",
        ),
        name='password_change_done'
    ),
    # url-адреса сброса пароля
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            form_class=forms.CustomPasswordResetForm,
            success_url=reverse_lazy("account:password_reset_done"),
            template_name="registration/password_reset_form.html",
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            form_class=forms.CustomPSetPasswordForm,
            template_name="registration/password_reset_confirm.html",
            success_url=reverse_lazy("account:password_reset_complete"), 
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
           template_name="registration/password_reset_complete.html",
        ),
        name='password_reset_complete'
    ),
    path('register/', views.register, name="register"),
    path("", views.dashboard, name="dashboard"),
]


