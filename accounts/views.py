from django.shortcuts import render

def sign_up(request):
    return render(request, 'sign_up.html')

def log_in(request):
    return render(request, 'log_in.html')

def log_out(request):
    return render(request, 'log_out')
