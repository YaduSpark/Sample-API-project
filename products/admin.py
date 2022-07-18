from django.contrib import admin

from .models import PurchaseRecord, category, manufacturer, product

# Register your models here.


@admin.register(category, manufacturer, product, PurchaseRecord)
class ProductAdmin(admin.ModelAdmin):
    pass
