from django.db import models
from django.contrib.auth import get_user_model
from apps.users.models import User


def user_directory_path(instace, filname):
    return 'users/socialposts/{0}'.format(filname)
def comment_directory_path(instace, filname):
    return 'users/commentposts/{0}'.format(filname)

class SocialPost(models.Model):

    shared_body = models.TextField(blank = True, null = True)
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "share", null = True, blank = True) 

    body = models.TextField()
    image = models.ImageField(upload_to = user_directory_path, blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'social_post_author')
    likes = models.ManyToManyField(get_user_model(), blank = True, related_name = 'likes')

    def __str__(self):
        return ("author: {}, date: {}").format(self.author, self.created_on.strftime('%H:%M:%S %d/%m/%Y'))

class SocialComment(models.Model):
    comment = models.TextField()
    image = models.ImageField(upload_to = comment_directory_path, blank = True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'social_comment_author')
    likes = models.ManyToManyField(User, blank = True, related_name = 'comment_likes')
    social_post = models.ForeignKey(SocialPost, on_delete = models.CASCADE, related_name = 'social_post_comment')

    def __str__(self):
        return self.comment