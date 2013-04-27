from django.shortcuts import render

def index(request):
  return render(request, 'index/index.html', {})

def welcome(request):
  return render(request, 'index/welcome.html', {})

def about(request):
  return render(request, 'index/about.html', {})

def beta(request):
  return render(request, 'index/beta.html', {})

def login(request):
  return render(request, 'index/login.html', {})

def signup(request):
  return render(request, 'index/signup.html', {})