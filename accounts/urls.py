from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', views.logout_user),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile')
]
