import stripe
from django.conf import settings
import requests
from rest_framework import status
from config.settings import STRIPE_SECRET_KEY
from education import serializers
from education.models import Payment

# def checkout_session(paid_course, user):
#     headers = {'Authorization': f'Bearer {settings.STRIPE_SECRET_KEY}'}
#     data = [
#         ('amount', paid_course.price),
#         ('currency', 'usd'),
#     ]
#     response = requests.post('https://api.stripe.com/v1/payment_intents', headers=headers, data=data)
#     if response.status_code != status.HTTP_200_OK:
#         raise Exception(f'ошибка : {response.json()["error"]["message"]}')
#     payment_intent = response.json()
#     return {'id': payment_intent['id']}
#
#
# def create_payment(paid_course, user):
#     payment = Payment.objects.create(
#         user=user,
#         paid_course=paid_course,
#         payment_amount=paid_course.price
#     )
#     return payment

from dotenv import load_dotenv
import os
import requests


def create_payment(amount: float) -> str:
    """Create a payment"""
    headers = {'Authorization': f"Bearer {STRIPE_SECRET_KEY}"}
    params = {
        'amount': amount,
        'currency': 'usd',
        'automatic_payment_methods[enabled]': 'true',
        'automatic_payment_methods[allow_redirects]': 'never'
    }
    url = 'https://api.stripe.com/v1/payment_intents'
    response = requests.post(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('id')
    else:
        return response.json().get('error')


def retrieve_payment(payment_intent_id: str) -> dict:
    """Retrieve a payment"""
    headers = {'Authorization': f"Bearer {STRIPE_SECRET_KEY}"}
    url = f'https://api.stripe.com/v1/payment_intents/{payment_intent_id}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("status")


def make_payment(payment_intent_id: str) -> dict:
    """Make a payment"""
    headers = {'Authorization': f"Bearer {STRIPE_SECRET_KEY}"}
    params = {'payment_method': 'pm_card_visa'}
    url = f'https://api.stripe.com/v1/payment_intents/{payment_intent_id}/confirm'
    response = requests.post(url, headers=headers, params=params)
    if response.status_code == 200:
        if response.json().get('status') == 'succeeded':
            return response.json().get('status')
    else:
        return response.json().get('error')
