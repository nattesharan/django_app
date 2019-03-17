from django.shortcuts import redirect, reverse

def main(request):
    return redirect(reverse('login'))