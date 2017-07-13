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
from django.conf.urls import url
from django.contrib import admin
from MyBlog import views as v1
from MyUser import views as v2


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', v1.main_page, name='main_page'),
    url(r'^auth/register$', v2.register, name='register'),
    url(r'^auth/login$', v2.log_in, name='main_page'),
    url(r'^blog/posts$', v1.post_list, name='post_list'),
    url(r'^auth/blog_id$',v2.get_blog_id),
    url(r'^blog/post$',v1.show_add_selected_post,name='and_or_show_post_in_blog'),
    url(r'^blog/comments$',v1.show_comment,name='show_comment'),
    url(r'^blog/comment$',v1.add_comment,name='add_comment'),
]

