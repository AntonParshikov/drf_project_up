from django.core.management.base import BaseCommand
from users.models import User
from datetime import date
from education.models import Course, Lesson, Payment


class Command(BaseCommand):
    help = 'Create sample payment'

    def handle(self, *args, **options):
        user = User.objects.first()
        course = Course.objects.first()
        lesson = Lesson.objects.first()
        payment_date = date.today()
        payment_amount = 10000
        payment_method = 'Credit card'

        payment = Payment.objects.create(
            user=user,
            payment_date=payment_date,
            paid_course=course,
            paid_lesson=lesson,
            payment_amount=payment_amount,
            payment_method=payment_method
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created payment {payment.id}'))
