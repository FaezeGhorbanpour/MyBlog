from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from MyUser.models import MyUser



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('img', 'bio')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','password']