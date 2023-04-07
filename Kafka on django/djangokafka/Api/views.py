from kafka import KafkaProducer, KafkaConsumer
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from kafka import KafkaConsumer
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

# # Create a Kafka consumer instance for messages coming from Kafka topic

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# regular expression to match valid email address format
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def send_email(email, password, message, topic):
    try:
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = 'New Kafka message received'
        body = f'New message received on Kafka topic "{topic}":\n\n{message}'
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Error sending email: {e}')

def adil(consumer):
    for message in consumer:
        if message is None:
            continue

        message_str = message.value.decode()
        if not message_str.strip():
            continue

        data = json.loads(message_str)
        if not isinstance(data, dict):
            raise ValueError('Invalid message format: expected dictionary object')
        email = data.get('email')
        if not email or not re.match(email_regex, email):
            raise ValueError('Invalid email address format')
        password = data.get('password')
        
        message = data.get('message')
        topic = data.get('topic')

    
        send_email(email, password, message,topic)
    
consumer = KafkaConsumer('adil', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True)
adil(consumer)
