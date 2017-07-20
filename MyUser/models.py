from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUser(models.Model):
    user = models.OneToOneField(User)
    img = models.ImageField(upload_to='static/img/', default='static/img/no-img.jpg', blank=True)
    bio = models.TextField(default='',blank=True)

    def __str__(self):
        if self.user.first_name is None and self.user.last_name is None:
            return self.user.username
        else:
            return self.user.first_name + " - " + self.user.last_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

