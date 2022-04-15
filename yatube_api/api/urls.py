from django.urls import path, include
from rest_framework import routers

from .views import (PostViewSet,
                    CommentViewSet,
                    FollowViewSet,
                    GroupViewSet)


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]
