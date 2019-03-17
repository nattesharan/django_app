from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html',context)
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html',context)

def logout_user(request):
    logout(request)
    return redirect(reverse('main'))