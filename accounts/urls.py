from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', views.logout_user),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password')
]
