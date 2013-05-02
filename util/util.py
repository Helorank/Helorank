from accounts.models import Account

def get_logged_in_user(request):
  if "account_id" in request.session:
    account_id = request.session["account_id"]
    account = Account.get(id=account_id)
    return account
  else:
    return False
  