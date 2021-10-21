from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))

    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))
    
    class Meta:
        model = User
        fields = 'username', 'password'

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))

    email = forms.CharField(widget=EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты',
    }))

    first_name = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))

    last_name = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию',
    }))

    password1 = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))

    password2 = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
