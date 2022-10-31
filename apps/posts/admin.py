from django.contrib import admin
from apps.posts.models import SocialPost, SocialComment

admin.site.register(SocialPost)
admin.site.register(SocialComment)
