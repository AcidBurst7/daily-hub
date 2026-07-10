from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, 
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm
)
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': 'Ваш никнейм',
            'email': 'Ваш e-mail',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        required=True, 
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    username = forms.CharField(
        required=True, 
        label="Логин",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    agree_to_terms = forms.BooleanField(
        required=True,  # Делает поле обязательным для заполнения
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label=mark_safe(
            'Регистрируясь, я принимаю условия <a href="/terms/" target="_blank">Пользовательского соглашения</a> '
            'и даю согласие на обработку моих персональных данных в соответствии с '
            '<a href="/privacy/" target="_blank">Политикой конфиденциальности</a>.'
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "email",
        )
    

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            # "form-label"


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "old_password": "Текущий пароль",
            "new_password1": "Новый пароль",
            "new_password2": "Подтверждение нового пароля",
        }

        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": placeholders[name]
            })


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class CustomPSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
