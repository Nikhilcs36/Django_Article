from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, LoginUserForm, PasswordChangingForm
from django.contrib.auth import authenticate, login, logout
from main.models import Blog
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created successfully.")
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, "Error")
    else:
        form = SignupForm()
    return render(request, "auth/signup.html", {'form': form})
        

def user_login(request):
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
    return render(request, "auth/login.html", {"login_form":form})

def user_logout(request):
    logout(request)
    messages.success(request,"you have successfully logout")
    return redirect('home')

def profile(request, user_name):
    user_related_data = Blog.objects.filter(auther__username = user_name)
    context = {
       "user_related_data":user_related_data 
    }
    return render(request, "auth/profile.html", context)
    

class PasswordChageView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password-success')
    
def password_success(request):
    return render(request, "auth/password_change_success.html")
