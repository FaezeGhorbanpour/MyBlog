from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from MyUser.models import MyUser



class Post(models.Model):
    title = models.CharField(max_length=200, null=False, default='The topic is not specified!')
    date = models.DateTimeField(default=timezone.now,blank=True)
    blog = models.ForeignKey('Blog',on_delete=models.CASCADE, null=True)
    text = models.TextField(default='Text not written!', blank=True)
    summery = models.TextField(default='Summary not written!')
    image = models.ImageField(upload_to='MyBlog/static/img/post/', default='MyBlog/static/img/no-img.jpg',name='')

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
    number = models.IntegerField(blank=True,null=False,default=0)
    auther = models.ForeignKey(MyUser,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='MyBlog/static/img/Blog/', default='static/img/no-img.jpg')

    def __str__(self):
        return self.auther.user.username + ' : ' + str(self.number)

@receiver(pre_save,sender = Blog)
def setCount(sender, instance,*args, **kwargs):
    instance.number = Blog.objects.filter(auther= instance.auther).count()+1

