from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    user_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_name')

    imagen = models.ImageField("imagen", upload_to='perfil/', blank = True, null = True)

    followers = models.ManyToManyField(User, blank = True, related_name = 'followers')

    following = models.ManyToManyField(User, blank = True, related_name = 'following')

    date_created = models.DateField(auto_now_add=True)

    #user info

    location = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)


    def __str__(self):
        return self.user.username