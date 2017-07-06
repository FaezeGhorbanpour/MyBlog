from django import forms
from .models import Post


class PostForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text')


class NameForm (forms.Form):
    your_name = forms.CharField(label='Your name')