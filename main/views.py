from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def signup(request) :
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)  
            return redirect('profile')
    else :
        form = CustomUserCreationForm() 
    return render(request, 'main/signup.html', {'form': form})
    
def profile(request) :
    if not request.user.is_authenticated :
        return redirect('login')
    return render(request , 'main/profile.html' , {'user' : request.user})

def dashboard(request) :
    if not request.user.is_authenticated:
       return redirect('login') 

    return render(request , 'main/dashboard.html' ,{'username' : request.user.username} )