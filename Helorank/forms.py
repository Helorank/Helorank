from django import forms

class LogInForm(forms.Form):
  email = forms.EmailField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)

  def clean_email(self):
    # Trim, lowercase password
    email = self.cleaned_data.get('email').strip().lower()
    return email
    