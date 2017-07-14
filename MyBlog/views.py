from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from MyUser.views import get_blog_id
from .models import Post

@login_required
def each_post(request):
    return render(request, 'blog/blog_page.html')


def start_page(request):
    return render(request, 'blog/start_page.html')


def main_page(request):
    return render(request, 'blog/main_page.html')


@csrf_exempt
@login_required
def post_list(request, number):
    if default_token_generator.check_token(request.user, request.META.get('HTTP_X_TOKEN')):
        offset = request.GET.get('offset')
        count = request.GET.get('count')
        blog_id = get_blog_id(request, number)
        if offset and count:
            posts = Post.objects.filter(blog=blog_id)[int(offset):int(offset) + int(count)]
        elif count:
            posts = Post.objects.filter(blog=blog_id)[:int(count)]
        elif offset:
            posts = Post.objects.all(blog=blog_id)[int(offset):int(offset) + 5]
        else:
            posts = Post.objects.all(blog=blog_id)
        status = 0
        posts = serializers.serialize("json", posts)
        return JsonResponse({
            'status': status,
            'posts': posts
        })
    else:
        return JsonResponse({
            'status': -1
        })


@login_required
def show_add_selected_post(request):
    if request.method == 'GET':
        pass


@login_required
def show_comment(request):
    pass


@login_required
def add_comment(request):
    pass
