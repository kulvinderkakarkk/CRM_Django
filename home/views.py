from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def redirect_home(request):
    if request.user.is_authenticated:
        return redirect('customer.list')
    else:
        return redirect('home.login')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer.list')
        else:
            messages.error(request, 'There was an issue with login.. Please try again')
            return redirect('home.login')
    return render(request, 'user_login.html', {})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out..')
    return redirect('home.login')

def user_register(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('customer.list')
    return render(request, 'user_register.html', {'form':form})
