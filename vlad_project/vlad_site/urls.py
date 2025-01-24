"""
URL configuration for vlad_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about_page, name='about'),
    path('about/python', views.python_about_view, name='about_python'),
    path('about/csharp', views.csharp_about_view, name='about_csharp'),
    path('about/php', views.php_about_view, name='about_php'),
    path('about/ht', views.html_about_view, name='about_html'),
    path('about/ruby', views.ruby_about_view, name='about_ruby'),
    path('about/java', views.java_about_view, name='about_java'),
    path('about/js', views.javascript_about_view, name='about_js'),

    # AUTHS
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
