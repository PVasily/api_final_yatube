from django.urls import path, include
from rest_framework import routers

from .views import (PostViewSet,
                    CommentViewSet,
                    FollowViewSet,
                    GroupViewSet)


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt'))
]
