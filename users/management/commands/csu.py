from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@test.ru',
            first_name='test',
            last_name='test',
            role='visitor',
            is_superuser=False,
            is_staff=False,
            is_active=True

        )

        user.set_password('324214Kross!')
        user.save()
