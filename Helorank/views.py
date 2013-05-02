from django.shortcuts import render, redirect

def index(request):
  return render(request, 'index/construction.html', {})

def signUp(request):

  return render(request, 'index/signUp.html', {})
  
def welcome(request):
  return render(request, 'index/welcome.html', {})

def logout(request):
  # Delete all session data
  request.session.flush()
  return redirect('/welcome')