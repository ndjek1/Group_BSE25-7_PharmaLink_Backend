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
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not email or not password:
            self.stdout.write(self.style.ERROR(
                'ADMIN_EMAIL and ADMIN_PASSWORD environment variables must be set.'
            ))
            return

        if not User.objects.filter(email=email).exists():
            self.stdout.write(self.style.SUCCESS(f'Creating superuser: {email}'))
            User.objects.create_superuser(email=email, password=password)
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{email}" already exists.'))
