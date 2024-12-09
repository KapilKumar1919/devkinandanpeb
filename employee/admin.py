from django.contrib import admin
from django.utils.safestring import mark_safe
from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'emp_code',
        'name', 
        'designation',
        'mobile',
        # 'display_image',
        )
    list_filter = (
        'designation',
        'gender',
        )
    list_per_page = 10

    search_fields = ('name', 'mobile')

    # @staticmethod
    # def display_image(self, obj):
    #     if obj.logo:
    #         return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.logo.url))
    #     return 'No Image'
