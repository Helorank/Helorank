from django.shortcuts import render
from django.contrib.auth.hashers import *
from accounts.models import Account

# Create your views here.
def create_account_handler(request):
  if request.method == 'GET':
    return create_account_handler_get(request)
  elif request.method == 'POST':
    return create_account_handler_post(request)
  

def create_account_handler_get(request):
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
    return render(request,'accounts/accountCreated.html',{ "account" : newAccount })
