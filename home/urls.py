from django.conf.urls import url
from home.views import home, HomeView, connect_friends

urlpatterns = [
    # url(r'^$', home, name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^connect/(?P<action>.+)/(?P<pk>\d+)/$', connect_friends, name='connect-friends')
]