from rest_framework import routers
from api.views import UserView

router = routers.DefaultRouter()

router.register(r'^users', UserView)

urlpatterns = router.urls