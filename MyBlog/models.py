from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    summery = models.TextField()


    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.text