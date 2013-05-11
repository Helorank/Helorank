from accounts.models import Account
from django import forms

class SignUpForm(forms.Form):
  min_password_length = 6
  username = forms.CharField(max_length=50)
  email = forms.EmailField(max_length=100)
  password = forms.CharField(min_length=min_password_length, max_length=100, widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  def clean_username(self):
    # Check current usernames
    username = self.cleaned_data.get('username')
    if Account.objects.filter(username=username):
      raise forms.ValidationError('Username has already been used')
    return username

  def clean_email(self):
    # Trim, lowercase password. Check current accounts
    email = self.cleaned_data.get('email')
    if Account.objects.filter(email=email):
      raise forms.ValidationError('Email has already been used')
    return email.strip().lower()

  def clean_confirm_password(self):
    # Validate password against confirm_password
    password = self.cleaned_data.get('password')
    confirm_password = self.cleaned_data.get('confirm_password')
    if not password:
      return u'supressed'
    else:
      if not confirm_password:
        raise forms.ValidationError('Please confirm your password')
      if password != confirm_password:
        print password
        raise forms.ValidationError('Passwords do not match')
      return u'confirmed'
    