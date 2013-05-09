from django import forms

class SignUpForm(forms.Form):
  min_password_length = 6
  email = forms.EmailField(max_length=100)
  password = forms.CharField(min_length=min_password_length, max_length=100, widget=forms.PasswordInput)
  confirm_password = forms.CharField(min_length=min_password_length, max_length=100, widget=forms.PasswordInput)
  age = forms.IntegerField(required=False)
  username = forms.CharField(max_length=50)
  first_name = forms.CharField(required=False, max_length=50)
  last_name = forms.CharField(required=False, max_length=50) 

  def clean_confirm_password(self):
    # Validate password againt confirm_password
    password = self.cleaned_data.get('password')
    confirm_password = self.cleaned_data.get('confirm_password')
    if not confirm_password:
        raise forms.ValidationError("You need to confirm your password")
    if password != confirm_password:
        raise forms.ValidationError("Your passwords do not match")
    return u'confirmed'

class LogInForm(forms.Form):
  email = forms.EmailField(max_length=100)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)