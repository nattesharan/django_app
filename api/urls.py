from rest_framework import routers
from django.conf.urls import url
from api.views import UserView, posts, post_detail

router = routers.DefaultRouter()

router.register(r'^users', UserView)

urlpatterns = router.urls
urlpatterns += [
    url(r'^posts/$', posts, name='posts'),
    url(r'^posts/(?P<pk>\d+)/$', post_detail, name='post_detail')
]