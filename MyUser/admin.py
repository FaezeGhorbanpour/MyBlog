from django.contrib import admin
from MyUser.models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




UserAdmin.list_display = ('username','first_name', 'last_name', 'email', 'is_active', 'date_joined', 'is_staff')

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('user','bio','img',)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(MyUser,MyUserAdmin)
