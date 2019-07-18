from django.shortcuts import render, redirect, reverse
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import datetime
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = "Sharan"
    context = {
        'numbers': numbers,
        'name': name
    }
    
    return render(request, 'accounts/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html',context)
    else:
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html',context)

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('main'))


def view_profile(request, pk=None):
    if pk:
        logger.info('Viewing profile for {}'.format(pk))
        context = {
            'user': User.objects.get(pk=pk)
        }
    else:
        logger.info('Viewing own profile')
        context = {
            'user': request.user,
            'last_visit': request.COOKIES.get('last_visit', datetime.datetime.utcnow()),
            'visits': request.COOKIES.get('visits', 0)
        }
    # print(request.session.get('username','Not found'))
    # if request.session.test_cookie_worked():
    #     print("The test cookie worked!!!")
    #     request.session.delete_test_cookie()
    return render(request, 'accounts/profile.html', context=context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance = request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # if we dont add this the usr will be logged out after changing password
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        form = form
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})