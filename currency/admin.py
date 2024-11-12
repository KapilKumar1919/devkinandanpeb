from django.contrib import admin

from currency import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    ordering = ('code',)
    list_display = (
        'code', 'display_name',
        'symbol', 'base_currency',
    )
    search_fields = (
        'code', 'display_name',
    )

