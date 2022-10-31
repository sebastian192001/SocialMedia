from django.db import router
from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserViewset, ProfileViewset

router = DefaultRouter()

router.register(r'users',UserViewset)
router.register(r'Profiles',ProfileViewset)

urlpatterns = router.urls
