from django.shortcuts import render, redirect, reverse
from accounts.forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserChangeForm
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

def logout_user(request):
    logout(request)
    return redirect(reverse('main'))

def view_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context=context)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
        form = form
    else:
        form = UserChangeForm(instance = request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})
    