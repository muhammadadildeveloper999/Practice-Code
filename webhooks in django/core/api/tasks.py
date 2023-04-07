# tasks.py
import os
import json
import requests
from celery import shared_task, Celery
from django.conf import settings
from datetime import timedelta
from rest_framework.views import APIView

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@shared_task
def send_webhook_notification():
        try:
            # Build the message
            event_type = 'This is a webhook notification'
            user_name = 'Muhammad Adil'
            message = f'{user_name} just triggered event {event_type}!'

            # Send the notification
            response = requests.post(
                'https://webhook.site/046f8b3a-88a4-4355-9b8f-29b75e6e622f',
                data=json.dumps({'message': message}),
                headers={'Content-Type': 'application/json'},
                timeout=None
            )

            # Check the response and log the result
            if response.ok:
                print('Webhook notification sent successfully')
            else:
                print('Failed to send webhook notification')
        except Exception as e:
            print(f'Error sending webhook notification: {e}')


# Schedule the task to run every 2 minutes
app.conf.beat_schedule = {
    'send-webhook-notification-every-2-minutes': {
        'task': 'core.tasks.send_webhook_notification',
        'schedule': timedelta(minutes=2),
    },
}

