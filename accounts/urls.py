from django.conf.urls import url
# password_reset helps to send email and password_reset_done shows check your email to reset password
from django.contrib.auth.views import (
    login, 
    password_reset, 
    password_reset_done, 
    password_reset_confirm, 
    password_reset_complete
)
from . import views
urlpatterns = [
    # url(r'^$', views.home, name="home"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_user_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {
        'template_name': 'accounts/reset_password.html', 
        'post_reset_redirect':'accounts:password_reset_done',
        'email_template_name': 'accounts/reset_password_template.html'
        }, name='reset-password'),
    url(r'^reset-password/done/$', password_reset_done, {
        'template_name': 'accounts/reset_password_done.html'
    }, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {
        'post_reset_redirect': 'accounts:password_reset_complete',
        'template_name': 'accounts/reset_password_confirm.html'
    }, name='password_reset_confirm'),
    url(r'^reset-password/complete', password_reset_complete, {
        'template_name': 'accounts/password_reset_complete.html'
    }, name='password_reset_complete')
]
