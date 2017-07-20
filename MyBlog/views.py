from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from MyBlog.forms import PostForm, CommentForm
from MyUser.models import MyUser
from MyUser.views import get_blog_id
from .models import Post, Comment
from django.utils.translation import get_language_info


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
        #print('showing posts !')
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

@csrf_exempt
@login_required
def show_add_selected_post(request,number):
    if default_token_generator.check_token(request.user, request.META.get('HTTP_X_TOKEN')):
        if request.method == 'GET':
            #print('showing one post !')
            post_id = request.GET.get('id')
            blog_id = get_blog_id(request, number)
            post = Post.objects.filter(blog=blog_id,id=post_id)
            post = serializers.serialize("json", post)
            return JsonResponse({
                'status': 0,
                'post': post
            })
        elif request.method == 'POST':
            #print('Adding Post !')
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.instance
                post.blog = list(get_blog_id(request, number))[0]
                post = post_form.save()
                post.refresh_from_db()
                status = 1
                messages = 'ok'
            else:
                status = -1
                messages = post_form.errors
            return JsonResponse({
                'status': status,
                'message': messages
            })




@csrf_exempt
@login_required
def show_comment(request, number):
    if default_token_generator.check_token(request.user, request.META.get('HTTP_X_TOKEN')) and request.method == 'GET':
        #print('showing comments !')
        offset = request.GET.get('offset')
        count = request.GET.get('count')
        post_id = request.GET.get('post_id')
        if offset and count:
            comments = Comment.objects.filter(post=post_id)[int(offset):int(offset) + int(count)]
        elif count:
            comments = Comment.objects.filter(post=post_id)[:int(count)]
        elif offset:
          comments = Comment.objects.filter(post=post_id)[int(offset):int(offset) + 5]
        else:
            comments = Comment.objects.filter(post=post_id)
        status = 0
        comments = serializers.serialize("json", comments)
        return JsonResponse({
            'status': status,
            'comments': comments
        })
    else:
        return JsonResponse({
            'status': -1
        })


@csrf_exempt
@login_required
def add_comment(request,number):
    if default_token_generator.check_token(request.user, request.META.get('HTTP_X_TOKEN')) and request.method == 'POST':
        #print('Adding Comment !')
        comment_form = CommentForm(request.POST)
        post_id = request.POST.get('post_id')
        if comment_form.is_valid():
            comment = comment_form.instance
            comment.post = list(Post.objects.filter(id=post_id))[0]
            comment.auther = list(MyUser.objects.filter(user=request.user))[0]
            #print(comment.auther)
            comment = comment_form.save()
            comment.refresh_from_db()
            status = 1
            messages = 'ok'
        else:
            status = -1
            messages = comment_form.errors
        return JsonResponse({
            'status': status,
            'message': messages
        })

