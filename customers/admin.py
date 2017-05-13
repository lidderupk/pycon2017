from django.contrib import admin

from . import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['admin_name']


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'placed_at', 'shipped_at', 'shipped', 'total']
    list_editable = ['shipped']
    list_filter = ['shipped', 'placed_at', 'shipped_at']
    ordering = ['placed_at']

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.PurchaseItem)
