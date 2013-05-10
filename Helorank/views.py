from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib.auth.hashers import *
from django.core.context_processors import csrf
from util.util import *
import accounts.forms
import hashlib

#Add a session wrapper. Distinguish account from user

def under_construction(request):
  return render(request, 'index/under_construction.html')

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
  
def logout(request):
  # Delete all session data
  request.session.flush()
  return redirect('/')
  
def welcome(request):
  current_user = get_logged_in_user(request)
  if current_user:
    return render(request, 'accounts/dashboard.html', {'account': current_user})
  else:  
    return render(request, 'index/welcome.html', {})

