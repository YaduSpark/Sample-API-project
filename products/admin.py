from django.contrib import admin

from .models import category, manufacturer, product

# Register your models here.


@admin.register(category, manufacturer, product)
class ProductAdmin(admin.ModelAdmin):
    pass
