from django.urls import path
from authors import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('user-profile/<str:user_name>/', views.profile, name="profile"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]
