from django.shortcuts import render

def index(request):
  return render(request, 'index/construction.html', {})
  
def login(request):
  return render(request, 'index/login.html', {})
  
def logout(request):
  # Delete all session data
  request.session.flush()
  return render(request, 'index/welcome.html', {})

def signUp(request):
  return render(request, 'index/signUp.html', {})
  
def welcome(request):
  return render(request, 'index/welcome.html', {})



