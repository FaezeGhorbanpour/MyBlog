from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, default='The topic is not specified!')
    date = models.DateTimeField(default=now())#.strftime('%c')
    auther = models.ForeignKey('User')
    text = models.TextField()
    summery = models.TextField(default='Summary not written!')
    image = models.ImageField(upload_to='static/img/', default='static/img/no-img.jpg')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    auther = models.ForeignKey('User')
    date = models.DateTimeField(default=now())#.strftime('%c'))

    def __str__(self):
        return self.text

class User(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50, null=False, default='First name is not specified')
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.DateTimeField(default=now())#.strftime('%c')
    #posts = models.ForeignKey('Post')

    def __str__(self):
        if self.last_name is None:
            return self.first_name
        else:
            return self.first_name + " " + self.last_name
