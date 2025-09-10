# apps/users/management/commands/createsuperuser_if_none_exists.py

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    """
    Create a superuser if one does not exist.
    This is useful for automating deployment.
    """
    help = 'Create a superuser if one does not exist'

    def handle(self, *args, **options):
        # Get the superuser credentials from environment variables
        username = os.environ.get('ADMIN_USER')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not username or not password or not email:
            self.stdout.write(self.style.ERROR(
                'ADMIN_USER, ADMIN_EMAIL, and ADMIN_PASSWORD environment variables must be set.'
            ))
            return

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Creating superuser: {username}'))
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))