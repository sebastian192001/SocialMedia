from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  
from apps.posts.api.serializers import PostSerializer, CommentSerializer

class PostViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = PostSerializer.Meta.model.objects.all()

class CommentViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = CommentSerializer.Meta.model.objects.all()
