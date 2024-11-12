from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from country.models import Country
from currency.models import Currency
from django.utils.text import slugify

class JobStatus(models.TextChoices):
    RECEIVED = 'received', _('Received')
    QUOTED = 'quoted', _('Quoted')
    ADVANCED_RECEIVED = 'advanced_received', _('Advanced Received')
    WORK_STARTED = 'work_started', _('Work Started')
    COMPLETED = 'completed', _('Completed')

class Company(models.Model):
    business_name = models.CharField(
        _('Business Name'),
        max_length=255
    )
    business_address = models.TextField(
        _('Business Address'),
    )
    logo = models.ImageField(
        upload_to='company/company_logos/',
        null=True,
        blank=True
    )
    name = models.CharField(
        _('Name'),
        max_length=255
    )
    gst = models.CharField(
        _('GST'),
        max_length=15
    )
    city = models.CharField(
        _('City'),
        max_length=255
    )
    state = models.CharField(
        _('State'),
        max_length=255
    )
    zip_code = models.CharField(
        _('Zip Code'),
        max_length=20
    )
    phone = models.CharField(
        _('Phone'),
        max_length=10,
        null=True,
        blank=True
    )
    email = models.EmailField(
        _('Email')
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='currencies',
        verbose_name=_('Currency')
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='countries',
        verbose_name=_('Country')
    )
    countries_serving = models.ManyToManyField(
        Country, 
        related_name='companies', 
        blank=True,
        verbose_name=_('Countries Serving')
    )
    established_date = models.DateField(
        _('Established Date'),
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='business_created', 
        verbose_name=_('Created by')
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='business_updated', 
        verbose_name=_('Updated by')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name=_('Updated at')
    )

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.business_name

    def years_of_establishment(self):
        if self.established_date:
            today = date.today()
            establishment_year = self.established_date.year
            current_year = today.year
            years_of_establishment = current_year - establishment_year
            return years_of_establishment
        else:
            return None

    def count_selected_countries(self):
        return self.countries_serving.count()

class JobType(models.Model):
    name = models.CharField(
        _('Job Type Name'),
        max_length=255
    )

    class Meta:
        verbose_name = _('Job Type')
        verbose_name_plural = _('Job Types')

    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(
        'Company', 
        on_delete=models.CASCADE, 
        related_name='jobs', 
        verbose_name=_('Company')
    )
    client = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        related_name='jobs_client',
        verbose_name=_('Client')
    )
    job_type = models.ForeignKey(
        'JobType', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name='jobs_job_type',
        verbose_name=_('Job Type')
    )
    services = models.ManyToManyField(
        'Service',
        related_name='jobs_services',
        verbose_name='Services'
    )
    title = models.CharField(
        _('Job Title'),
        max_length=255
    )
    slug = models.SlugField(
        _('Slug'),
        unique=True,
        max_length=255, 
        blank=True
    )
    description = models.TextField(
        _('Job Description')
    )
    start_date = models.DateField(
        _('Start Date')
    )
    end_date = models.DateField(
        _('End Date'),
        blank=True, 
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=JobStatus.choices,
        default=JobStatus.RECEIVED,
        verbose_name=_('Job Status')
    )
    quoted_amount = models.FloatField(
        _('Quoted Amount'),
        null=True,
        blank=True,
        default=0.0
    )
    advance_payment = models.FloatField(
        _('Adv. Payment'),
        null=True,
        blank=True,
        default=0.0
    )
    total_payment = models.FloatField(
        _('Total Payment'),
        null=True,
        blank=True,
        default=0.0
    )
    total_area_covered = models.CharField(
        _('Total Area Covered'),
        max_length=255,
        null=True,
        blank=True
    )
    remarks = models.CharField(
        _('Remarks'),
        max_length=255,
        null=True,
        blank=True
    )
    quotation_file = models.FileField(
        _('Quotation File'),
        null=True,
        blank=True
    )
    total_working_hours = models.PositiveIntegerField(
        _('Working Hours'),
        null=True,
        blank=True
    )
    work_location = models.CharField(
        _('Work Location'),
        max_length=255,
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='job_created', 
        verbose_name=_('Created by')
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='job_updated', 
        verbose_name=_('Updated by')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name=_('Updated at')
    )
    
    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class JobImage(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='job_images',
        verbose_name=_('Job')
    )
    image = models.ImageField(
        _('Image'),
        upload_to='job_images/'
    )

    class Meta:
        verbose_name = _('Job Image')
        verbose_name_plural = _('Job Images')

    def __str__(self):
        return f"{self.job.title} - Image {self.id}"

class Service(models.Model):
    name = models.CharField(
        _("Service Name"),
        max_length=255,
        null=True,
        blank=True
    )
    description = models.TextField(
        _("Service Description"),
    )
    image = models.ImageField(
        _('Image'),
        upload_to='service_images/'
    )

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

class Client(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='clients',
        verbose_name=_('Company')
    )
    name = models.CharField(
        _('Client Name'),
        max_length=255
    )
    email = models.EmailField(
        _('Client Email')
    )
    phone = models.CharField(
        _('Client Phone'),
        max_length=10
    )
    client_business_logo = models.ImageField(
        upload_to='company/company_logos/',
        null=True,
        blank=True
    )
    gst = models.CharField(
        _('GST'),
        max_length=15
    )
    city = models.CharField(
        _('City'),
        max_length=255
    )
    state = models.CharField(
        _('State'),
        max_length=255
    )
    zip_code = models.CharField(
        _('Zip Code'),
        max_length=20
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='client_countries',
        verbose_name=_('Country')
    )
    client_since = models.IntegerField(
        _('Client Since (Months)'),
        editable=False,
        default=0,
        help_text=_('Automatically incremented on a monthly basis.')
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True, 
        related_name='client_created', 
        verbose_name=_('Created by')
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='client_updated', 
        verbose_name=_('Updated by')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name=_('Updated at')
    )

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Calculate the duration in months and update the client_since field
        if self.created_at:
            duration = timezone.now() - self.created_at
            self.client_since = duration.days // 30  # Assuming an average of 30 days in a month
        super(Client, self).save(*args, **kwargs)

    def total_quoted_value(self):
        total_revenue = self.jobs_client.aggregate(Sum('quoted_amount'))['quoted_amount__sum']
        return total_revenue if total_revenue is not None else 0.0

    def total_revenue(self):
        total_revenue = self.jobs_client.filter(status=JobStatus.COMPLETED).aggregate(Sum('total_payment'))['total_payment__sum']
        return total_revenue if total_revenue is not None else 0.0

class Contact(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=255
    )
    mobile = models.CharField(
        _("Mobile"),
        max_length=10
    )
    email = models.EmailField(
        _("Email"),
    )
    subject = models.CharField(
        _("Subject"),
        max_length=255,
        )
    message = models.TextField(
        _("Message")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_('Created at')
    )

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.subject

class Quotation(models.Model):
    company_name = models.CharField(
        _("Company Name"),
        max_length=255
    )
    contact_person = models.CharField(
        _("Contact Person"),
        max_length=255
    )
    email = models.EmailField(
        _("Email"),
    )
    contact_no = models.CharField(
        _("Contact No"),
        max_length=10
    )
    address = models.TextField(
        _("Address"),
        blank=True, 
        null=True
    )
    subject = models.CharField(
        _("Subject"),
        max_length=255,
        blank=True, 
        null=True
    )
    remark = models.TextField(
        _("Remark"),
        blank=True, 
        null=True
    )
    plan_file = models.FileField(
        _("Plan File"),
        upload_to='quotations/plan_files/', 
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = _('Received Quotation')
        verbose_name_plural = _('Received Quotations')

    def __str__(self):
        return f"{self.company_name} - {self.contact_person}"
