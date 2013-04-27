from django.shortcuts import render

def index(request):
  return render(request, 'index/index.html', {})

def welcome(request):
  return render(request, 'index/welcome.html', {})