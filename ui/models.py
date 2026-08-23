from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Suggestions(models.Model):
    message = models.TextField(max_length=100)
    rating = models.IntegerField()
    def __str__(self):
        return self.message[:50] + "..."

def UploadPfp(instance, filename):
    ext = filename.split('.')[-1]
    newFilename = f"{instance.user.username}.{ext}"
    return os.path.join("profile_pics", newFilename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=15, blank=True, default="No bio added.")
    profile_picture = models.ImageField(upload_to=UploadPfp, null=True, blank=True, default="profile_pics/default_user.png")
    strikes = models.IntegerField(default=0)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    
    def __str__(self):
        return self.user.username + "'s profile"

class Post(models.Model):
    poster = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2500)
    image = models.ImageField(upload_to="images", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)