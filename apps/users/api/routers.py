from rest_framework.routers import DefaultRouter

from apps.users.api.api_views import user_api_view

router = DefaultRouter()

router.register('', user_api_view, basename='users')

urlpatterns = router.urls