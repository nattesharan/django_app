from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from home.forms import HomeForm
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        request.session.set_test_cookie()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})