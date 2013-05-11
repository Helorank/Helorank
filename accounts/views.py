from accounts.models import Account
from django.contrib.auth.hashers import *
from django.core.context_processors import csrf
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
    return render(request, 'index/login.html')

def signup(request):
  if request.method == 'POST':
    form = accounts.forms.SignUpForm(request.POST)
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
    form = accounts.forms.SignUpForm()
  return render(request, 'accounts/signup.html', {'form': form})
