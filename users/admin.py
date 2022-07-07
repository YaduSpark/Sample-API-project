from django.contrib import admin

from .models import newUser, Profile

# Register your models here.
@admin.register(newUser, Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass