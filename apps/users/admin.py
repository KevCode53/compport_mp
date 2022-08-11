from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from apps.core.models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
  ordering = ['id']
  list_display = ('email', 'username', 'name', 'last_name', 'phone', 'is_active', 'is_staff')
  fieldsets = (
    (None, {'fields': ('email', 'username', 'password')}),
    
    (_('Personal Info'), {'fields': ( 'name', 'last_name', 'phone', 'image')}),
    
    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    
    (_('Important Dates'), {'fields': ('last_login',)}),
  )

  # add_fieldsets = (
  #   (None, {
  #     'classes': ('wide',),
  #     'fields': ('email', 'username', 'password1', 'password2')
  #   })
  # )

admin.site.register(User, UserAdmin)