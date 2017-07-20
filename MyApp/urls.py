"""MyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from MyBlog import views

urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^StartPage.html$', views.start_page, name='start_page'),
    url(r'^main_page.html$', views.main_page, name='main_page'),
    url(r'^blog_page.html$', views.each_post, name='each_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/',include('MyUser.urls')),
    url(r'^blog/',include('MyBlog.urls')),
]

