from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from home.models import Post
from home.forms import HomeForm
import datetime
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created_on')
        users = User.objects.all()
        # sessions are also usually cookies but they arent stored in the client side they are stored in the server database
        # they are more secure than cookies
        # likewise cookies they too have expiry time
        # SESSION_COOKIE_AGE is the age of session cookies, in seconds.
        # Default: 1209600 (2 weeks, in seconds)
        if 'username' not in request.session:
            request.session['username'] = request.user.username
        response = render(request, self.template_name, {'form': form, 'posts': posts, 'users': users})
        # by default cookie expiry time is 1 year
        # request.session.set_test_cookie()
        # Expires sets an expiry date for when a cookie gets deleted
        # response.set_cookie('last_visit',datetime.datetime.utcnow(),max_age=30) in int is seconds
        # Max-age sets the time in seconds for when a cookie will be deleted (use this, it’s no longer 2009)
        # response.set_cookie('last_visit',datetime.datetime.utcnow(),expires=datetime) specify datetime of when to expire
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