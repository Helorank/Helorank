from accounts.models import Account
from django.contrib.auth.hashers import *
from django.core.context_processors import csrf
from django.shortcuts import render
from util.util import *
from accounts import forms
import hashlib


def dashboard(request):
  current_user = get_logged_in_user(request)
  return render(request, 'accounts/dashboard.html', { 'account': current_user})

def signup(request):
  if request.method == 'POST':
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
      cleaned_form = form.cleaned_data
      email = cleaned_form['email']
      username = cleaned_form['username']
      encrypted_password = make_password(cleaned_form['password'])
      gravatar_hash = hashlib.md5(email).hexdigest()
      newAccount = Account(email = email, username = username, password = encrypted_password, gravatar_hash = gravatar_hash, influence = 0)
      newAccount.save()
      request.session['account_id'] = newAccount.id
      context = { 'account' : newAccount }
      context.update(csrf(request))
      return render(request,'accounts/dashboard.html', context)
  else:
    form = forms.SignUpForm()
  return render(request, 'accounts/signup.html', {'form': form})
