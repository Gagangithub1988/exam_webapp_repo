from django.contrib import admin
from testApp.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=['email','username','last_login','date_joined','is_staff','is_admin','is_active']



    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account,AccountAdmin)