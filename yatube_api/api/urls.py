from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Версия API указывается здесь
    path('v1/', include(v1_router.urls)),
    # Добавляем путь для получения токена
    path('v1/api-token-auth/', obtain_auth_token),
]
