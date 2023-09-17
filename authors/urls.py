from django.urls import path
from authors import views

urlpatterns = [
    # path('signup/', views.signup, name="signup"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    
    # path('user-profile/<str:user_name>/', views.profile, name="profile"),
    path('user-profile/<str:user_name>/', views.Profile.as_view(), name="profile"),
    
    # path('login/', views.user_login, name="login"),
    path('login/', views.UserLogin.as_view(), name="login"),
    
    # path('logout/', views.user_logout, name="logout"),
    path('logout/', views.UserLogout.as_view(), name="logout"),
    
    path('change_password/', views.PasswordChageView.as_view(template_name = "auth/password_change.html"),
    name="change-password"),
    path('password_success/', views.password_success, name="password-success"),
    path('edit_profile/', views.UpdateUserView.as_view(), name="edit-user"),
    path('delete_user/<int:pk>/', views.DeleteUser.as_view(), name="delete_user"),
]
