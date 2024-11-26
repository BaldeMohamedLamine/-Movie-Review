from django.contrib import admin
from django.http import HttpRequest

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request ,obj=None):
        return True

    def has_delete_permission(self, request , obj = None):
        return True
admin.site.register(User,UserAdmin)
