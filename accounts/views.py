from django.shortcuts import render, redirect, reverse
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


def logout_user(request):
    logout(request)
    return redirect(reverse('main'))