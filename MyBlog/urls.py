from django.conf.urls import url
from MyBlog import views

urlpatterns = [
    url(r'^(?P<number>[0-9]+)/posts/$', views.post_list, name='post_list'),
    url(r'^(?P<number>[0-9]+)/post/$', views.show_add_selected_post, name='and_or_show_post_in_'),
    url(r'^(?P<number>[0-9]+)/$comments/', views.show_comment, name='show_comment'),
    url(r'^(?P<number>[0-9]+)/comment/$', views.add_comment, name='add_comment'),
]