from country import models
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        if models.Country.objects.count() == 0:
            call_command('loaddata', 'fixtures/countries.json')

