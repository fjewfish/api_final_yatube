from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
