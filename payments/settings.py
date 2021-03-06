from django.conf import settings

"""
Payment process update order email notification.
"""
PAYMENT_PROCESS_EMAIL_NOTIFY = getattr(settings, 'PAYMENT_PROCESS_EMAIL_NOTIFY', False)

FIO_BANK_TOKEN = getattr(settings, 'FIO_BANK_TOKEN', 'token')
FIO_BANK_PROCESS_DAYS = 3

PAYMENT_ERROR_RATE = getattr(settings, 'PAYMENT_ERROR_RATE', 0)

PAYPAL_ADDITIONAL_CHARGE = getattr(settings, 'PAYPAL_ADDITIONAL_CHARGE', 2)
PAYPAL_MODE = getattr(settings, 'PAYPAL_MODE', 'sandbox')
PAYPAL_CLIENT_ID = getattr(settings, 'PAYPAL_CLIENT_ID', 'client_id')
PAYPAL_CLIENT_SECRET = getattr(settings, 'PAYPAL_CLIENT_SECRET', 'secret')
