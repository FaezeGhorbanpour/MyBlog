from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core import serializers

# Create your views here.

def main_page(request):
    return render(request, 'blog/main_page.html')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.time = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})


def post_edit(request,pk):
    post = get_object_or_404(Post,pk)
    if request.method == 'POST':
        edit_post = PostForm(request.POST,instance=post)
        if edit_post.is_valid():
            edit_post.save(commit=False)
            edit_post.author = request.user
            edit_post.time = timezone.now()
            edit_post.save()
            return redirect('blog/post_detail.html',pk=edit_post.pk)
    else:
        edit_post = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'post':post})

def post_list(request):
    offset = request.GET.get('offset')
    count = request.GET.get('count')
    if  offset and count:
        posts = Post.objects.all()[int(offset):int(offset)+int(count)]
    elif count:
        posts = Post.objects.all()[:int(count)]
    elif offset:
        posts = Post.objects.all()[int(offset):int(offset) + 5]
    else:
        posts = Post.objects.all()

    posts = serializers.serialize("json", posts)
    print(posts)
    return HttpResponse(posts, content_type='application/json')



def register(request):
    pass

def login(request):
    pass