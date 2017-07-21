from django import forms
from MyBlog.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','summary','text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']