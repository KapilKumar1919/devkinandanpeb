from django.contrib import admin
from country import models

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name', 'code')
    list_display = (
        'name', 'code',
        'phone_code', 'region',
        'sub_region',
    )

