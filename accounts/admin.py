from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .models import Profile

admin.site.login = login_required(admin.site.login)


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
