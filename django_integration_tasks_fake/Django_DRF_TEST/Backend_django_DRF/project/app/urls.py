from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet, RegisterView

# 🔥 Create router
router = DefaultRouter()

# Register ViewSets
router.register(r'jobs', JobViewSet, basename='jobs')
router.register(r'applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    # Router URLs (auto CRUD)
    path('', include(router.urls)),

    # Custom API
    path('register/', RegisterView.as_view()),
]