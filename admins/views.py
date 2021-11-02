from django.http import response
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

# Create your views here.

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'Geekshop - admins',
    }
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):

    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            print(form.errors)

    else:
        form = UserAdminRegistrationForm()

    context = {
        'title': 'Geekshop - admins: create user',
        'form': form,
    }

    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_read(request):
    context = {
        'title': 'Geekshop - admins: select users',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, user_id):

    selected_user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {
        'title': 'Geekshop - admins: update user',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, user_id):
    selected_user = User.objects.get(id=user_id)
    #selected_user.delete()

    #selected_user.is_active = False
    #selected_user.save()

    selected_user.ban()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))

