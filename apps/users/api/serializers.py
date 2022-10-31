from rest_framework import serializers
from apps.users.models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'email', 
            'is_staff', 
            'is_active', 
            'date_joined'
        )

class ProfileSerializer(serializers.ModelSerializer):

    user_name = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
     )
    
    following = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
     )

    followers = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
     )

    class Meta:
        model = Profile
        fields = (
            'id', 
            'user', 
            'user_name',
            'imagen', 
            'date_created', 
            'location',  
            'birthday', 
            'bio', 
            'followers', 
            'following'
        )
