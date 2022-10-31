from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  
from apps.users.api.serializers import UserSerializer, ProfileSerializer

class UserViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

class ProfileViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()
