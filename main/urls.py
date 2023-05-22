from django.urls import path
from main import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about_us/', views.about, name="about"),
    
]