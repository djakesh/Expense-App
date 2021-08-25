from django.contrib import admin

# Register your models here.
from users.models import Account

admin.site.register(Account)