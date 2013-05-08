from django.contrib import admin
from accounts.models import Account

class AccountAdmin(admin.ModelAdmin):
  list_display = ('email', 'first_name', 'last_name',)

admin.site.register(Account, AccountAdmin)