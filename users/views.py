from django.shortcuts import render, redirect
from home.models import *
from home.forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import hashlib

def index(request):

    topics = Topic.objects.all()
    form = RegisterUser()

    return render(request, 'userCreate.html', {'topics': topics, 'form': form})

def save(request):

    topics = Topic.objects.all()
    
    if(request.method == 'POST'):

        form = RegisterUser(request.POST)
        message_success = ""
        message_fail = ""

        if form.is_valid():
            form.save()

            message_success = "Account created successfully"
        else:
            message_fail = "Failed to create the account."

        return render(request, "userCreate.html", {'topics': topics, "message_success": message_success, "message_fail": message_fail,'form': form,})

    else:
        topics = Topic.objects.all()
        form = RegisterUser()

        return render(request, "userCreate.html", {'topics': topics, "message":"Failed to create the account.",'form': form})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.warning(request, "Authentication failed")

    return  render(request, ('index.html'))

def user_logout(request):

    logout(request)

    return redirect('home')

def make_password(password):
    assert password
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hash

def check_password(hash, password):
    """Generates the hash for a password and compares it."""
    generated_hash = make_password(password)
    return hash == generated_hash
