from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
        "last_login",
    )
    list_display_links = ("email",)
    readonly_fields = ("date_joined", "last_login")
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 25


admin.site.register(Account, AccountAdmin)
