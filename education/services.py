import stripe
from django.conf import settings
import requests
from rest_framework import status
from config.settings import STRIPE_SECRET_KEY
from education.models import Payment


def checkout_session(paid_course, user):
    headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}
    data = [
        ('amount', paid_course.price),
        ('currency', 'usd'),
    ]
    response = requests.post('https://api.stripe.com/v1/payment_intents', headers=headers, data=data)
    if response.status_code != status.HTTP_200_OK:
        raise Exception(f'ошибка : {response.json()["error"]["message"]}')
    payment_intent = response.json()
    return {'id': payment_intent['id']}


def create_payment(paid_course, user):
    Payment.objects.create(
        user=user,
        paid_course=paid_course,
        payment_amount=paid_course.price
    )
