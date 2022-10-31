from django.db import router
from rest_framework.routers import DefaultRouter
from apps.posts.api.views import PostViewset, CommentViewset

router = DefaultRouter()

router.register(r'posts',PostViewset)
router.register(r'comments',CommentViewset)

urlpatterns = router.urls
