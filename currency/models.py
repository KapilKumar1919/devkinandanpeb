from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    id = models.BigAutoField(
        _('ID'),
        primary_key=True
    )
    code = models.CharField(
        _('currency code'),
        max_length=20,
        unique=True
    )
    display_name = models.CharField(
        _('currency display name'),
        max_length=100
    )
    base_currency = models.BooleanField(
        _('base currency'),
        default=True
    )
    symbol = models.CharField(
        _('currency symbol'),
        max_length=50,
        default=''
    )
    description = models.CharField(
        _('currency description'),
        max_length=250,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
        db_table = 'Currency'

    def __str__(self):
        return f'{self.display_name} ({self.code})'
