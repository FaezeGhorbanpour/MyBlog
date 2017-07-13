from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from MyUser.forms import UserForm, ProfileForm
from .models import Post
from django.core import serializers
from django.contrib.auth import login, authenticate



def main_page(request):
    return render(request, '../templates/blog/start_page.html')


def post_list(request):
    offset = request.GET.get('offset')
    count = request.GET.get('count')
    blog_id = request.GET.get('blog_id')
    if not blog_id :
        if  offset and count:
            posts = Post.objects.all()[int(offset):int(offset)+int(count)]
        elif count:
            posts = Post.objects.all()[:int(count)]
        elif offset:
            posts = Post.objects.all()[int(offset):int(offset) + 5]
        else:
            posts = Post.objects.all()
    else:
        if offset and count:
            posts = Post.objects.filter(blog=blog_id)[int(offset):int(offset)+int(count)]
        elif count:
            posts = Post.objects.filter(blog=blog_id)[:int(count)]
        elif offset:
            posts = Post.objects.all(blog=blog_id)[int(offset):int(offset) + 5]
        else:
            posts = Post.objects.all(blog=blog_id)

    posts = serializers.serialize("json", posts)
    return HttpResponse(posts, content_type='application/json')

def show_add_selected_post(request):
    if request.method == 'GET':
        pass

def show_comment(request):
    pass
def add_comment(request):
    pass
