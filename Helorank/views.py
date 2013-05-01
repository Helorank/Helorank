from django.shortcuts import render

def index(request):
  return render(request, 'index/Construction.html', {})

def SignUp(request):
  return render(request, 'index/SignUp.html', {})
  
def Welcome(request):
  return render(request, 'index/Welcome.html', {})