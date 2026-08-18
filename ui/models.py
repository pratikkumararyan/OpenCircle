from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestions(models.Model):
    message = models.TextField(max_length=100)
    rating = models.IntegerField()
    def __str__(self):
        return self.message[:50] + "..."

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=15, blank=True, default="No bio added.")
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True, default="profile_pics/default_user.png")
    strikes = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username + "'s profile"

