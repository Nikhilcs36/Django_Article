from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from main.models import Blog
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your account was created successfully.")
#             new_user = authenticate(
#                 username = form.cleaned_data['username'],
#                 password = form.cleaned_data['password1'],
#             )
#             login(request, new_user)
#             return redirect('home')
#         else:
#             messages.error(request, "Error")
#     else:
#         form = SignupForm()
#     return render(request, "auth/signup.html", {'form': form})

class SignUp(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy("login")
    success_message = "User has been created, please login with your username and password"
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "please enter data properly")
        return redirect('signup')
        

# def user_login(request):
    # if request.method == "POST":
    #     form = LoginUserForm(request, data = request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
            
    #         user = authenticate(username = username , password = password)
            
    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, f"you are logged in as {username}")
    #             return redirect('home')
    #         else:
    #             messages.error(request, "Error")
    #     else:
    #         messages.error(request, "username or password is incorrect")
    # form = LoginUserForm()  
    # return render(request, "auth/login.html", {"login_form":form})

class UserLogin(generic.View):
    form_class = LoginUserForm
    template_name = "auth/login.html"
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                
                user = authenticate(username = username , password = password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, f"you are logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "username or password is incorrect")
        form = LoginUserForm()  
        return render(request, "auth/login.html", {'form':form})
        
    

# def user_logout(request):
#     logout(request)
#     messages.success(request,"you have successfully logout")
#     return redirect('home')

class UserLogout(LoginRequiredMixin, generic.View):
    login_url = 'login'
    def get(self, request):
        logout(request)
        messages.success(request,"User logged out")
        return redirect('home')
        

# def profile(request, user_name):
#     user_related_data = Blog.objects.filter(auther__username = user_name)
#     context = {
#        "user_related_data":user_related_data 
#     }
#     return render(request, "auth/profile.html", context)

class Profile(LoginRequiredMixin, generic.View):
    model = Blog
    login_url = 'login'
    template_name = "auth/profile.html"
    
    def get(self, request, user_name):
        user_related_data = Blog.objects.filter(auther__username = user_name)
        context = {
        "user_related_data":user_related_data 
        }
        return render(request, self.template_name, context)
        
    
class PasswordChageView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'login'
    success_url = reverse_lazy('password-success')
    
def password_success(request):
    return render(request, "auth/password_change_success.html")


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    login_url = 'login'
    template_name = "auth/edit_user_profile.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"
    
    def get_object(self):
        return self.request.user
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "please enter data carefully")
        return redirect('home')
    

class DeleteUser(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = User
    login_url = 'login' #for Restrict user "login_url" and "LoginRequiredMixin"
    template_name = "auth/delete_user_confirm.html"
    success_message = "User has been deleted"
    success_url = reverse_lazy('home')