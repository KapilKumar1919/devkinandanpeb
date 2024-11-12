from django.core.management import call_command
from django.core.management.base import BaseCommand

from currency import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        if models.Currency.objects.count() == 0:
            call_command('loaddata', 'fixtures/currencies.json',)

