from django.urls import path
from .views import CreateTokenView, CreateUserView
from apps.users.api.api_views import user_api_view, user_detail_view

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('users/', user_api_view, name='user'),
    path('users/<int:pk>', user_detail_view, name='user_detail'),
]
