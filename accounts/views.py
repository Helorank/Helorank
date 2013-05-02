from django.shortcuts import render
from django.contrib.auth.hashers import *
from accounts.models import Account
from django.core.context_processors import csrf
from util.util import *

# Create your views here.
def dashboard(request):
  user = get_logged_in_user(request)
  if user:
    print "User: " + user.email
  return render(request, 'accounts/dashboard.html', {})
  
def create_account_handler(request):
  if request.method == 'GET':
    return create_account_handler_get(request)
  elif request.method == 'POST':
    return create_account_handler_post(request)

def create_account_handler_get(request):
  user = get_logged_in_user(request)
  return render(request,'accounts/createAccount.html',{ "error" : "No error"})

def create_account_handler_post(request):
  post_dict = request.POST
  email = post_dict["email"]
  #Check for already used password
  if Account.objects.filter(email=email):
    # e-mail has already been used
    return render(request, 'accounts/createAccount.html',{ "error" : "E-mail has already been used" })
  else:
    password = post_dict["password"]
    username = post_dict["username"]
    encrypted_password = make_password(password)
    print encrypted_password
    newAccount = Account(email = email, username=username, password=encrypted_password)
    newAccount.save()
    request.session["account_id"] = newAccount.id
    print "New Account ID: " + str(newAccount.id)
    context = { "account" : newAccount }
    context.update(csrf(request))
    return render(request,'accounts/accountCreated.html',context)
