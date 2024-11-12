from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if get_user_model().objects.count() == 0:
            get_user_model().objects.create_superuser(
                username='admin',
                password='admin',
            )
            print('Admin accounts created successfully.')
