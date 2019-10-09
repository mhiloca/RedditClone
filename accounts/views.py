from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from posts.models import Post

def sign_up(request):
    """ Registers user and redirects to login page """
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')

def log_in(request):
    """ Logs in user and redirects to dashboard """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def dashboard(request):
    """ Shows all posts by user """
    id = request.user.id
    posts = Post.objects.filter(posted_by__id=id)

    context = {
        'posts': posts
    }

    return render(request, 'accounts/dashboard.html', context)
