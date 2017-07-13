from django.contrib import admin

# Register your models here.
from MyUser.models import MyUser

admin.site.register(MyUser)