
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.db import transaction
from django.http import JsonResponse

from .forms import ProfileForm, LoginForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@transaction.atomic
def register(request):
    if request.method == 'POST':
        print ('Registering ...')
        print (request)
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST,
                                       instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
            status = 1
            messages = 'ok'
        else:
            status = request.POST
            messages= user_form.error_messages
        return JsonResponse({
            'status': status,
            'message':messages
        })


@csrf_exempt
@transaction.atomic
def log_in(request):
    print('Logging in ...')
    print (request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active :
                login(request, user)
                status = 1
                messages = 'ok'
                token = default_token_generator.make_token(user)
            else:
                status = 0
                messages = "You're account is disabled."
        else:
            status = 0
            messages= "invalid login details " + username + " " + password
        return JsonResponse({
            'status': status,
            'message':messages,
            'token' : token
        })

def get_blog_id(request):
    pass
