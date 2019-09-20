from django.shortcuts import render, redirect

def dashboard(request):

    return render(request, 'myproject/dashboard.html')

def index(request):

    return render(request, 'myproject/index.html')

def login(request):

    return render(request, 'myproject/login.html')

def signup(request):

    return render(request, 'myproject/signup.html')

def form(request):

    return render(request, 'myproject/form.html')
