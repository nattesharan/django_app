from rest_framework import routers
from django.conf.urls import url
from api.views import UserView, posts, post_detail, PostsApiView, PostsGenericView, LoginApiView, LogoutApiView
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()

router.register(r'^users', UserView)

urlpatterns = router.urls
urlpatterns += [
    url(r'^posts/$', posts, name='posts'),
    url(r'^posts/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    # I dont want to have multiple classess for handling details and list separately so I'll change the route accordingly
    url(r'^cposts/$', PostsApiView.as_view(), name='class_posts_api'),
    url(r'^cposts/(?P<pk>\d+)/$', PostsApiView.as_view(), name='class_post_details_api'),
    url(r'^gposts/$', PostsGenericView.as_view(), name='generic_posts_get'),
    url(r'^gposts/(?P<pk>\d+)/$', PostsGenericView.as_view(), name='generic_post_detail'),
    # but they may be cases where we want to have our own LoginView
    url(r'^auth/login/$',ObtainAuthToken.as_view(), name='auth_token_view'),
    # custom auth token login and logout
    url(r'^auth/me/login/$', LoginApiView.as_view(), name='login_api'),
    url(r'^auth/me/logout/$', LogoutApiView.as_view(), name='logout_api')
]