from django.conf.urls import url
from MyBlog import views

urlpatterns = [
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^post/$', views.show_add_selected_post, name='and_or_show_post_in_'),
    url(r'^comments/$', views.show_comment, name='show_comment'),
    url(r'^comment/$', views.add_comment, name='add_comment'),
]