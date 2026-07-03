from django.db import models

class Suggestions(models.Model):
    message = models.TextField(max_length=200)
    rating = models.IntegerField()
   
