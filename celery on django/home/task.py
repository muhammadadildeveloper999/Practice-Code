from core.celery import app
from .models import *
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.conf import settings

@app.task(name="send_notification")
def send_notification():
    
    time_thresold = datetime.now() - timedelta(hours=2)

    profile_objs = profile.objects.filter(is_verified=False,created_at__gte = time_thresold)
    print(profile_objs)
    for profile_obj in profile_objs:
        subject = "Notificationyou Account Is Not Verified"
        message = "Your Account Is Not Verified"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [profile_obj.email]
        send_mail(subject , message , email_from , recipient_list)