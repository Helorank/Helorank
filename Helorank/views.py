from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib.auth.hashers import *
from django.core.context_processors import csrf
from util.util import *
from Helorank import forms

def login(request):
  current_user = get_logged_in_user(request)
  if current_user:
    return redirect('/account/dashboard')
  else:
    error = u''
    if request.method =="POST":
      form = forms.LogInForm(request.POST)
      if form.is_valid():
        cleaned_form = form.cleaned_data
        email  = cleaned_form['email']
        password = cleaned_form['password']
        try:
          account = Account.objects.get(email=email)
          if check_password(password,account.password):
            # Successful login
            request.session["account_id"] = account.id
            return redirect('/account/dashboard')
          else:
            error = u'Password does not match'
        except Account.DoesNotExist:
          error = u'Account does not exist'
    else:
      form = forms.LogInForm()
    return render(request, 'index/login.html', {'form': form, 'error': error})

def requires_login(view):
  def new_view(request, *args, **kwargs):
    current_user = get_logged_in_user(request)
    if not current_user:
      return redirect('/login')
    return view(request, *args, **kwargs)
  return new_view
  
def logout(request):
  # Delete all session data
  request.session.flush()
  return redirect('/')

def under_construction(request):
  return render(request, 'index/under_construction.html')
