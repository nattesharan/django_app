from django.conf.urls import url
from home.views import home, HomeView

urlpatterns = [
    # url(r'^$', home, name='home'),
    url(r'^$', HomeView.as_view(), name='home')
]