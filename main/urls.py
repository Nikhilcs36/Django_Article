from django.urls import path
from main import views

urlpatterns = [
    path('', views.blog_home, name="blog_home"),
    path('blog_detail/', views.blog_detail, name="blog_detail"),
    path('profile/', views.profile, name="profile"),
    
]