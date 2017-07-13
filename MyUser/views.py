from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import ProfileForm, LoginForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfileForm(request.POST,
                                       instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            status = 1
            messages = 'ok'
        else:
            status = request.POST
            messages= user_form.error_messages
        return JsonResponse({
            'status': status,
            'message':messages
        })
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()


@csrf_exempt
@transaction.atomic
def log_in(request):
    print (request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active :
                login(request, user)
                status = 1
                messages = 'ok'
            else:
                status = 0
                messages = "You're account is disabled."
        else:
            status = 0
            messages= "invalid login details " + username + " " + password
        return JsonResponse({
            'status': status,
            'message':messages
        })

def get_blog_id(request):
    pass
