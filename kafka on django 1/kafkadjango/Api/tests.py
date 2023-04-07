from django.test import TestCase

# Create your tests here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from kafka import KafkaProducer
import json
import jwt
from rest_framework.views import APIView
from .models import Super_AdminAcount

# Define the login function to authenticate the user
class Login(APIView):
    def post(self,request):
        Email = request.data['Email']
        Password = request.data['Password']
        fetchuser = Super_AdminAcount.objects.filter(Email = Email).first()
        if fetchuser and handler.verify(Password,fetchuser.Password):
            # if not fetchuser.status == "Disable":
                access_token_payload = {
                    "Id":fetchuser.Id,
                    "Fname":fetchuser.Fname,
                    "Lname":fetchuser.Lname,
                    "Role":fetchuser.Role,
                    "Email":fetchuser.Email,
                    "ContactNo":fetchuser.ContactNo,
                }
                access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm='HS256')
                return HttpResponse(access_token, status=200)
        else:
            return HttpResponse("Invalid login credentials", status=401)

@csrf_exempt
def send_message_to_kafka(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            topic = data.get('topic')
            message_text = data.get('message')
            email = data.get('email')

            if not topic or not message_text or not email:
                return HttpResponse('Error: Missing required keys. Payload must include "email", "topic", and "message" keys.')

            message = {'email': email, 'topic': topic, 'text': message_text}
        except ValueError as e:
            print(f'Invalid JSON format: {e}')
            return HttpResponse('Invalid message format')

        # Authenticate the user before sending a message to Kafka
        try:
            access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return HttpResponse('Token has expired', status=401)
        except jwt.InvalidTokenError:
            return HttpResponse('Invalid token', status=401)

        if not payload:
            return HttpResponse('Invalid token', status=401)

        # send the dynamic message content to Kafka
        try:
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
            producer.send(topic, json.dumps(message).encode('utf-8'))
            producer.flush()
            print(f"Message '{email}' sent to topic '{email}'")
        except Exception as e:
            print(f'Error sending message to Kafka: {e}')
            return HttpResponse('Error sending message to Kafka')

        return HttpResponse('Message sent to Kafka')
    else:
        return HttpResponse('Invalid request method')
