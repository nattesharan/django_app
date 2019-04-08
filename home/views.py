from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from home.forms import HomeForm
import datetime
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        response = render(request, self.template_name, {'form': form})
        # request.session.set_test_cookie()
        visits = int(request.COOKIES.get('visits', 0))
        if 'last_visit' in request.COOKIES:
            last_visit = datetime.datetime.strptime(request.COOKIES['last_visit'][:-7],'%Y-%m-%d %H:%M:%S')
            if (datetime.datetime.utcnow() - last_visit).days > 0:
                response.set_cookie('last_visit',datetime.datetime.utcnow())
                response.set_cookie('visits', visits+1)
        else:
            response.set_cookie('last_visit',datetime.datetime.utcnow())
            response.set_cookie('visits', 0)
        return response
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})