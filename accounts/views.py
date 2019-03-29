from django.shortcuts import render, redirect, reverse
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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
            return redirect(reverse('home'))
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

@login_required
def view_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context=context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
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
            return redirect(reverse('view_profile'))
        form = form
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})