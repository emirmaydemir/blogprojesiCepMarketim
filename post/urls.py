
from django.urls import path
from .views import *
from post.views import post_index, post_detail
from django.urls import re_path
app_name='post'

urlpatterns = [
    re_path(r'index/$',post_index,name='index'),
    re_path(r'create/$',post_create,name='create'),

    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/update/', post_update, name='update'),
    path('<slug:slug>/delete/', post_delete, name='delete'),
]