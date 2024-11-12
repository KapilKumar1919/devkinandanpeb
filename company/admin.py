from django.contrib import admin
from django.utils.safestring import mark_safe

from company.models import Client, Company, Job, JobType, Contact, JobImage, Service, Quotation


class JobImageInline(admin.StackedInline):
    model = JobImage
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'business_name',
        'name',
        'gst',
        'city',
        'state',
        'country',
        'phone',
        'email'
    )
    search_fields = (
        'business_name',
        'name',
        'gst',
        'city',
        'state',
        'country',
        'phone',
        'email'
    )
    ordering = ('id',)

    @staticmethod
    def display_image(self, obj):
        if obj.logo:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.logo.url))
        return 'No Image'

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email', 
        'phone', 
        'city', 
        'state', 
        'country', 
        'total_quoted_value',
        'total_revenue',
    )
    search_fields = (
        'name', 
        'email', 
        'phone', 
        'city', 
        'state', 
        'country__name'
    )
    list_filter = (
        'state',
    )

    readonly_fields = ('get_total_revenue', 'get_total_quoted_value')

    def get_total_revenue(self, obj):
        return obj.total_revenue()

    get_total_revenue.short_description = 'Total Revenue'

    def get_total_quoted_value(self, obj):
        return obj.total_quoted_value()

    get_total_quoted_value.short_description = 'Total Quoted Amount'

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    ordering = ('id',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status', 'start_date', 'end_date', 'total_working_hours', 'updated_by', 'updated_at',)
    list_filter = ('company', 'status', 'start_date', 'end_date', 'client__name',)
    search_fields = ('title', 'description', 'client__name',)
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('id',)

    inlines = [JobImageInline]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'mobile',
        'email', 
        'subject',
    )
    search_fields = (
        'name',
        'mobile',
        'email',
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'contact_person',
        'email',
        'contact_no',
    )