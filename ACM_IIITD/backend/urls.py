from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("index", views.index, name="index"),
    path("members", views.members, name="members"),
    path('blogs', views.blog_home, name='blogHome'),
    path('blogs/<int:id>', views.blog, name='blog'),
]