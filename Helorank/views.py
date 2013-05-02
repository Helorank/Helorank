from django.shortcuts import render

def index(request):
  return render(request, 'index/Construction.html', {})

def signUp(request):
  return render(request, 'index/SignUp.html', {})
  
def welcome(request):
  return render(request, 'index/Welcome.html', {})

def logout(request):
  # Delete all session data
  request.session.flush()
  return render(request, 'index/Welcome.html', {})