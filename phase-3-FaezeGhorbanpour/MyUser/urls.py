
from django.conf.urls import url
from MyUser import views

urlpatterns = [
url(r'^register/$', views.register, name='register'),
url(r'^login/$', views.log_in, name='log_in'),
url(r'^blog_id/$',views.get_blog_id),
]