
from django.urls import path
from .views import *
from post.views import post_index, post_detail
from django.urls import re_path
app_name='accounts'

urlpatterns = [
    re_path(r'login/$',login_view,name='login'),
    re_path(r'register/$', register_view, name='register'),
    re_path(r'logout/$', logout_view, name='logout'),
]