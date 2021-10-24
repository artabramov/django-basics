from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket

# Create your views here.
def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    context = {
        'title': 'Geekshop - Логин',
        'description': 'Описание страницы логина',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration finished.')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)

    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Geekshop - Регистрация',
        'description': 'Описание страницы регистрации',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Geekshop - User profile',
        'description': 'User profile description',
        'baskets': Basket.objects.filter(user=request.user),
        'form': form,
    }
    return render(request, 'users/profile.html', context)
