from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from employee.views import upload_employee_details, download_employee_details
from company.views import upload_client_details, download_client_details

admin.site.site_header = 'Devkinandan - Pre-engineered Building'
admin.site.index_title = 'Applications'
admin.site.site_title = 'Devkinandan'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
    path('upload_employee_details/', upload_employee_details, name='upload_employee_details'),
    path('download_employee_details/', download_employee_details, name='download_employee_details'),
    path('upload_client_details/', upload_client_details, name='upload_client_details'),
    path('download_client_details/', download_client_details, name='download_client_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
