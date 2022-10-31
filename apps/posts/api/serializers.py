from rest_framework import serializers
from apps.posts.models import SocialPost, SocialComment
from apps.users.models import User

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
    )
    
    likes = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
    )


    class Meta:
        model = SocialPost
        fields = '__all__' 

class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
    )
    
    likes = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
    )

    
    class Meta:
        model = SocialComment
        fields = '__all__' 