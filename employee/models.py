from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    MARRIED = "Married"
    UNMARRIED = "Unmarried" 
    I_RATHER_DO_NOT_SAY = "I Rather Do Not Say" 
    
    MARITAL_CHOICES = [
        (MARRIED, "Married"),
        (UNMARRIED, "Unmarried"),
        (I_RATHER_DO_NOT_SAY, "I Rather Do Not Say"),
        ]
    
    M = "Male"
    F = "Female" 
    R = "I Rather Do Not Say" 

    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female'),
        (R, 'I Rather Do Not Say'),
    )
    
    emp_code = models.CharField(
        _('Emp Code'),
        max_length=100, 
        unique=True
    )
    name = models.CharField(
        _('Full Name'),
        max_length=100
    )
    date_of_joining = models.DateField(
        _('Date of Joining'),        
    )
    division = models.CharField(
        _('Division'),
        max_length=100,
        null=True,
        blank=True
    )
    designation = models.CharField(
        _('Designation'),
        max_length=255,
        null=True,
        blank=True
    )
    mobile = models.CharField(
        _('Mobile'),
        max_length=10,
        null=True,
        blank=True
    )
    emergency_contact = models.CharField(
        _('Emergency Contact'),
        max_length=10,
        null=True,
        blank=True
    )
    email = models.EmailField(
        _('Email'),
        null=True,
        blank=True
    )
    current_address = models.TextField(
        _('Current Address')
    )
    permanent_address = models.TextField(
        _('Permanent Address')
    )
    total_experience = models.FloatField(
        _('Total Experience'),
        null=True,
        blank=True,
        default=0.0
    )
    experience_with_new_company = models.FloatField(
        _('Experience with Us'),
        null=True,
        blank=True,
        default=0.0
    )
    marital_status = models.CharField(
        _('Marital Status'),
        max_length=50,
        choices=MARITAL_CHOICES,
        default=MARRIED
    )
    gender = models.CharField(
        _('Gender'),
        max_length=100,
        choices=GENDER_CHOICES,
        default=M
    )
    aadhar_card_number = models.CharField(
        _('Aadhar Card Number'),
        max_length=12,
        null=True,
        blank=True
    )
    pan_card = models.CharField(
        _('PAN'),
        max_length=10,
        null=True,
        blank=True
    )
    bank_name = models.CharField(
        _('Bank Name'),
        max_length=100,
        null=True,
        blank=True
    )
    bank_account_number = models.CharField(
        _('Bank Account Number'),
        max_length=100,
        null=True,
        blank=True
    )
    bank_ifsc = models.CharField(
        _('Bank IFSC'),
        max_length=11,
        null=True,
        blank=True
    )
    passport_image = models.ImageField(
        _('Image'),
        upload_to='employee/passport_image/',
        blank=True, 
        null=True
    )
    is_leader = models.BooleanField(
        _('Is Leader'),
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='employee_updated', 
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
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['emp_code']

    def __str__(self):
        return self.name
