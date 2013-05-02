from django.shortcuts import render

def index(request):
  return render(request, 'index/construction.html', {})

def signUp(request):
  return render(request, 'index/signUp.html', {})
  
def welcome(request):
  return render(request, 'index/welcome.html', {})