from rest_framework import routers
from django.conf.urls import url
from api.views import UserView, posts, post_detail, PostsApiView, PostsGenericView, LoginApiView, LogoutApiView,\
    AdminPermissionsView, AddPermissionView, PostsView, UserPosts
from rest_framework.authtoken.views import ObtainAuthToken
# for jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

router.register(r'^users', UserView)

# post_viewset = PostsView.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# we can add the above to url also but why do you want to ??
router.register(r'^vposts', PostsView)

urlpatterns = router.urls
urlpatterns += [
    url(r'^permissions/$', AdminPermissionsView.as_view(), name='permissions'),
    url(r'^add/permissions/$', AddPermissionView.as_view(), name='add_permissions'),
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
    url(r'^auth/me/logout/$', LogoutApiView.as_view(), name='logout_api'),
    url(r'^auth/token/$', TokenObtainPairView.as_view(), name='jwt_token_fetch'),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view(), name='jwt_refresh_fetch'),
    url(r'^user/posts/$', UserPosts.as_view(), name='user_posts')
]

# by default the access token has 5 mins of if access token is expired we use the refresh token to fetch new access token
# The refresh token is valid for the next 24 hours. 
# When it finally expires too, the user will need to perform a full authentication again using their username and password
# to get a new set of access token + refresh token.