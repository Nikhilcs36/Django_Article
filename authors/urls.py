from django.urls import path
from authors import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('user-profile/<str:user_name>/', views.profile, name="profile"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('change_password/', views.PasswordChageView.as_view(template_name = "auth/password_change.html"),
    name="change-password"),
    path('password_success/', views.password_success, name="password-success"),
    path('edit_profile/', views.UpdateUserView.as_view(), name="edit-user"),
]
