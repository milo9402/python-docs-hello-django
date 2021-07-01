from rest_framework import routers
from api.viewsets.user_viewset import UserViewSet

# from rest_framework.authtoken import views


router = routers.SimpleRouter()

router.register(r'user', UserViewSet)
urlpatterns = router.urls