from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(
        _('country name'),
        max_length=100
    )
    code = models.CharField(
        _('country code'),
        max_length=10
    )
    phone_code = models.CharField(
        _('country phone code'),
        max_length=50,
        null=True,
        blank=True
    )
    region = models.CharField(
        _('country region'),
        max_length=100,
        null=True,
        blank=True
    )
    sub_region = models.CharField(
        _('country sub region'),
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        db_table = 'CountryMaster'

    def __str__(self):
        return self.name


