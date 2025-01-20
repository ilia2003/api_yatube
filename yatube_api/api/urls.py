from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
