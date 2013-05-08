from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib.auth.hashers import check_password
from util.util import *
from settings import DEBUG

def index(request):
  if DEBUG:
    return render(request, 'index/construction.html')
  else:  
    return render(request, 'index/welcome.html')
  
# Login methods
def login(request):
  if request.method == "GET":
    return login_get(request)
  elif request.method == "POST":
    return login_post(request)

def login_get(request):
  return render(request, 'index/login.html', {})

def login_post(request):
  post_dict = request.POST
  email = post_dict["email"]
  password = post_dict["password"]
  try:
    account = Account.objects.get(email=email)
    if check_password(password,account.password):
      # Successful login
      request.session["account_id"] = account.id
      return redirect('/account/dashboard')
    else:
      # Password is incorrect
      print "Password didn't match."
      return render(request, 'index/login.html', { "error" : "Password did not match"})
  except Account.DoesNotExist:
    # If there is no account for that e-mail
    print "Account doesn't exist"
    return render(request, 'index/login.html', { "error" : "Username does not exist"})

# /Login Methods
  
def logout(request):
  # Delete all session data
  request.session.flush()
  return redirect('/welcome')

def signUp(request):
  return render(request, 'index/signUp.html', {})
  
def welcome(request):
  current_user = get_logged_in_user(request)
  if current_user:
    return render(request, 'accounts/dashboard.html', {'account': current_user})
  else:  
    return render(request, 'index/welcome.html', {})

