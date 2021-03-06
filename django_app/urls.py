"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth.decorators import login_required
from . import views

from graphene_django.views import GraphQLView
schema_view = get_swagger_view(title='API')

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^api/v1/', include('api.urls', namespace='api')),
    url(r'^api/docs/', schema_view),
    url(r'^graphapi/$', login_required(GraphQLView.as_view(graphiql=True))),
    # pubsub demo urls
    url(r'pubsub/$', views.publisher),
    url(r'pubsub/callback/$', views.pub_sub_callback)
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]