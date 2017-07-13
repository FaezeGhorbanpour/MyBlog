from django.db import models
from django.utils import timezone
from MyUser.models import MyUser



class Post(models.Model):
    title = models.CharField(max_length=200, null=False, default='The topic is not specified!')
    date = models.DateTimeField(default=timezone.now,blank=True)
    blog = models.ForeignKey('Blog',on_delete=models.CASCADE, null=True)
    text = models.TextField(default='Text not written!', blank=True)
    summery = models.TextField(default='Summary not written!')
    image = models.ImageField(upload_to='static/img/', default='static/img/no-img.jpg')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    auther = models.ForeignKey(MyUser,on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now,blank=True)#.strftime('%c'))

    def __str__(self):
        return self.text


class Blog(models.Model):
    auther = models.ForeignKey(MyUser,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='static/img/', default='static/img/no-img.jpg')

    def __str__(self):
        return self.auther.user.first_name + ' ' + self.auther.user.last_name