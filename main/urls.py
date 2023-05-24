from django.urls import path
from main import views

urlpatterns = [
    path('', views.blog_home, name="home"),
    path('blog_detail/', views.blog_detail, name="blog_detail"),
    path('user_profile/', views.profile, name="user_profile"),
    path('contact_us/', views.contact_us, name="contact_us"),
    # path('base.html/', views.base, name="base.html"),
    
]