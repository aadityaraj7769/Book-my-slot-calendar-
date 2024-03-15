from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a user with a specific ID'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user to be created')
        parser.add_argument('email', type=str, help='Email of the user to be created')
        parser.add_argument('password', type=str, help='Password of the user to be created')
        parser.add_argument('user_id', type=int, help='ID of the user to be created')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']
        user_id = kwargs['user_id']

        # Check if a user with the specified ID already exists
        if User.objects.filter(pk=user_id).exists():
            self.stdout.write(self.style.WARNING(f"A user with ID {user_id} already exists."))
        else:
            # Create a new user with the specified ID
            user = User.objects.create_user(username=username, email=email, password=password, id=user_id)
            self.stdout.write(self.style.SUCCESS(f"User '{username}' with ID {user_id} created successfully."))
