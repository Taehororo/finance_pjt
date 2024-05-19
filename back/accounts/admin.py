# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'postcode', 'road_address', 'jibun_address', 'detail_address')}),
    )

admin.site.register(User, CustomUserAdmin)