from django.contrib import admin
from MyUser.models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


#class MyUserAdmin(admin.ModelAdmin):
#    list_display = ('user.first_name', 'user.last_name', 'user.email')
#admin.site.register(MyUser,MyUserAdmin)

UserAdmin.list_display = ('username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('img','user','bio',)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(MyUser,MyUserAdmin)
