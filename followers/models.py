from django.db import models
from Users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class Followers(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')

    class Meta:
            unique_together = ('follower', 'following')


    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

