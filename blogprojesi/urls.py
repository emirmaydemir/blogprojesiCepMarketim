"""blogprojesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from post.views import home_view, post_index
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',home_view,name='home'),
    re_path(r'^post/', include('post.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)