from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.name
    class Meta:
        verbose_name_plural = 'userprofiles'
