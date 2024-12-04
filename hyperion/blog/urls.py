# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.blog_detail, name='post_detail.html'),
    path('post/new/', views.blog_list, name='blog_list'),
    path('post/<int:id>/edit/', views.signup, name='blog_edit'),
]
