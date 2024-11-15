# Generated by Django 5.0.2 on 2024-11-04 10:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
        ('currency', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('mobile', models.CharField(max_length=10, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Job Type Name')),
            ],
            options={
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('contact_person', models.CharField(max_length=255, verbose_name='Contact Person')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact_no', models.CharField(max_length=10, verbose_name='Contact No')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subject')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='Remark')),
                ('plan_file', models.FileField(blank=True, null=True, upload_to='quotations/plan_files/', verbose_name='Plan File')),
            ],
            options={
                'verbose_name': 'Received Quotation',
                'verbose_name_plural': 'Received Quotations',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Service Name')),
                ('description', models.TextField(verbose_name='Service Description')),
                ('image', models.ImageField(upload_to='service_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255, verbose_name='Business Name')),
                ('business_address', models.TextField(verbose_name='Business Address')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/company_logos/')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('gst', models.CharField(max_length=15, verbose_name='GST')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('zip_code', models.CharField(max_length=20, verbose_name='Zip Code')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('established_date', models.DateField(blank=True, null=True, verbose_name='Established Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('countries_serving', models.ManyToManyField(blank=True, related_name='companies', to='country.country', verbose_name='Countries Serving')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='country.country', verbose_name='Country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currencies', to='currency.currency', verbose_name='Currency')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Client Email')),
                ('phone', models.CharField(max_length=10, verbose_name='Client Phone')),
                ('client_business_logo', models.ImageField(blank=True, null=True, upload_to='company/company_logos/')),
                ('gst', models.CharField(max_length=15, verbose_name='GST')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('zip_code', models.CharField(max_length=20, verbose_name='Zip Code')),
                ('client_since', models.IntegerField(default=0, editable=False, help_text='Automatically incremented on a monthly basis.', verbose_name='Client Since (Months)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_countries', to='country.country', verbose_name='Country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='company.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Job Title')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Job Description')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('status', models.CharField(choices=[('received', 'Received'), ('quoted', 'Quoted'), ('advanced_received', 'Advanced Received'), ('work_started', 'Work Started'), ('completed', 'Completed')], default='received', max_length=20, verbose_name='Job Status')),
                ('quoted_amount', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Quoted Amount')),
                ('advance_payment', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Adv. Payment')),
                ('total_payment', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Total Payment')),
                ('total_area_covered', models.CharField(blank=True, max_length=255, null=True, verbose_name='Total Area Covered')),
                ('remarks', models.CharField(blank=True, max_length=255, null=True, verbose_name='Remarks')),
                ('quotation_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Quotation File')),
                ('total_working_hours', models.PositiveIntegerField(blank=True, null=True, verbose_name='Working Hours')),
                ('work_location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Work Location')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_client', to='company.client', verbose_name='Client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.company', verbose_name='Company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
                ('job_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs_job_type', to='company.jobtype', verbose_name='Job Type')),
                ('services', models.ManyToManyField(related_name='jobs_services', to='company.service', verbose_name='Services')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='JobImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='job_images/', verbose_name='Image')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_images', to='company.job', verbose_name='Job')),
            ],
            options={
                'verbose_name': 'Job Image',
                'verbose_name_plural': 'Job Images',
            },
        ),
    ]
