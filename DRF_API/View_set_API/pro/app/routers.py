from app.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'officers', UserViewSet, basename='officers')
urlpatterns = router.urls