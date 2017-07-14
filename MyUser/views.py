
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.db import transaction
from django.http import JsonResponse

from MyBlog.models import Blog
from MyUser.models import MyUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@transaction.atomic
def register(request):
    if request.method == 'POST':
        print ('Registering ...')
        user_form = UserCreationForm(request.POST)
        #profile_form = ProfileForm(request.POST)
        #print(user_form.data)
        #print(profile_form.data)
        if user_form.is_valid() :# and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            #profile_form = ProfileForm(request.POST)
           # profile_form.full_clean()
            #profile_form.save()
            myUser = MyUser.objects.get(user = user)
            default_blog = Blog(auther=myUser)
            default_blog.save()
            default_blog.refresh_from_db()
            status = 1
            messages = 'ok'
        else:
            status = -1
            messages= user_form.error_messages
        return JsonResponse({
            'status': status,
            'message':messages
        })


@csrf_exempt
@transaction.atomic
def log_in(request):
    print('Logging in ...')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        token = None
        if user is not None:
            if user.is_active :
                login(request, user)
                status = 0
                messages = 'ok'
                token = default_token_generator.make_token(user)
            else:
                status = -1
                messages = "You're account is disabled."
        else:
            status = -1
            messages= "invalid login details " + username
        return JsonResponse({
            'status': status,
            'message':messages,
            'token' : token
        })

def get_blog_id(request,number):
    return Blog.objects.filter(auther__user=request.user, number=number)
