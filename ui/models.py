from django.db import models

# Create your models here.
class Suggestions(models.Model):
    message = models.TextField(max_length=100)
    rating = models.IntegerField()
    def __str__(self):
        return self.message[:50] + "..."
    

