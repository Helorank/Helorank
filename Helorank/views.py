from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib.auth.hashers import *
from django.core.context_processors import csrf
from util.util import *
import accounts.forms
import hashlib

def index(request):
  return render(request, 'index/construction.html')
  
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

def new_sign_up(request):
  if request.method == 'POST':
    print unicode('test1')
    form = accounts.forms.SignUpForm(request.POST)
    if form.is_valid():
      print unicode('test2')
      cleaned_form = form.cleaned_data
      email = cleaned_form['email']
      if Account.objects.filter(email=email):
        return render(request, 'index/sign_up.html', {'form': form, 'error': 'Email has already been used'})
      else:
        username = cleaned_form['username']
        encrypted_password = make_password(cleaned_form['password'])
        gravatar_hash = hashlib.md5(email.strip().lower()).hexdigest()
        newAccount = Account(email = email, username=username, password=encrypted_password, gravatar_hash = gravatar_hash)
        newAccount.save()
        request.session['account_id'] = newAccount.id
        context = { 'account' : newAccount }
        context.update(csrf(request))
        return render(request,'accounts/dashboard.html',context)
  else:
    form = accounts.forms.SignUpForm()
  return render(request, 'index/sign_up.html', {'form': form})
  
def welcome(request):
  current_user = get_logged_in_user(request)
  if current_user:
    return render(request, 'accounts/dashboard.html', {'account': current_user})
  else:  
    return render(request, 'index/welcome.html', {})

