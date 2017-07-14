from django.contrib import admin
from .models import Post,Comment,Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','auther',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('auther','post','text','date')

class PostAdmin(admin.ModelAdmin):
    list_display = ('blog','title','summery','date')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Blog,BlogAdmin)


