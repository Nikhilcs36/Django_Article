from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your account was created successfully.")
#             return redirect('home')
#         else:
#             messages.error(request, "Error")
#     else:
#         form = UserCreationForm()
#     return render(request, "auth/signup.html", {'form': form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created successfully.")
            return redirect('home')
        else:
            messages.error(request, "Error")
    else:
        form = SignupForm()
    return render(request, "auth/signup.html", {'form': form})
        

def login(request):
    return render(request,"auth/login.html")
    
