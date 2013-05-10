from accounts.models import Account
from django.contrib.auth.hashers import *
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render
from util.util import *
import accounts
import hashlib

# Create your views here.
def dashboard(request):
  current_user = get_logged_in_user(request)
  if current_user:
    print "User: " + current_user.email
    return render(request, 'accounts/dashboard.html', {'account': current_user})
  else:
    return render(request, 'index/login.html', {'error': 'You are not logged in.'})

def signup(request):
  if request.method == 'POST':
    print unicode('test1')
    form = accounts.forms.SignUpForm(request.POST)
    if form.is_valid():
      print unicode('test2')
      cleaned_form = form.cleaned_data
      email = cleaned_form['email']
      if Account.objects.filter(email=email):
        return render(request, 'index/signup.html', {'form': form, 'error': 'Email has already been used'})
      else:
        username = cleaned_form['username']
        encrypted_password = make_password(cleaned_form['password'])
        gravatar_hash = hashlib.md5(email.hexdigest())
        newAccount = Account(email = email, username = username, password = encrypted_password, gravatar_hash = gravatar_hash)
        newAccount.save()
        request.session['account_id'] = newAccount.id
        print "New Account ID: " + str(newAccount.id)
        context = { 'account' : newAccount }
        context.update(csrf(request))
        return render(request,'accounts/dashboard.html',context)
  else:
    form = accounts.forms.SignUpForm()
  return render(request, 'index/signup.html', {'form': form})

# Placeholder for viewing friend profiles.
def profile(request, username):
  return HttpResponse('This feature is under construction. Please come back to view specific user profiles.')
