from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.http import streaminghttpresponse
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from passlib.hash import django_pbkdf2_sha256 as handler
from Api.models import*
from confluent_kafka import Producer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from kafka import KafkaProducer
import jwt
import json

KAFKA_TOPIC = 'your_kafka_topic'
KAFKA_CONSUMER_GROUP = 'your_kafka_consumer_group'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'


# create Kafka producer configuration
config = {
    'bootstrap.servers': 'localhost:9092',  # replace with actual Kafka broker address
}

# create Kafka producer instance
producer = Producer(config)



class signup(APIView):
    def post(self, request):
        password = request.data['password']
        email = request.data['email']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        phone = request.data['phone']
    
        data = account(firstname=firstname,lastname=lastname,phone=phone,
                                                                                        password=handler.hash(password), email = email)

        data.save()

        return Response({'status':True, 'msg':'SignUp successfully'})        


@csrf_exempt
def send_message_to_kafka(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            topic = data.get('topic')
            message = data.get('message')
            email = data.get('email')
            password = data.get('password')
            
            fetchuser = account.objects.filter(email=email).first()
            if fetchuser and handler.verify(password,fetchuser.password):
                
                if not topic or not message or not email or not password:
                    return HttpResponse('Error: Missing required keys. Payload must include "email", "topic", and "message" keys.')
                
                access_token_data = {
                    "firstname":fetchuser.firstname,
                    "lastname":fetchuser.lastname,
                    "email":fetchuser.email,
                    "email":fetchuser.email,
                    "phone":fetchuser.phone,
                }

                access_token = jwt.encode(access_token_data, str(config('SUPERADMIN_JWT_TOKEN')), algorithm='HS256')
                data = {'firstname':fetchuser.firstname,'lastname':fetchuser.lastname,'phone':fetchuser.phone,'email':fetchuser.email, 'Login_As':(email)}

            else:
                return HttpResponse("Invalid login credentials", status=401)

            message = {'email': email, 'topic': topic, 'message': message, 'password':password}

        except ValueError as e:
            print(f'Invalid JSON format: {e}')
            return HttpResponse('Invalid message format')

        # send the dynamic message content to Kafka
        try:
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
            producer.send(topic, json.dumps(message).encode('utf-8'))
            producer.flush()
            print(f"Message '{email}' sent to topic '{topic}'")
        except Exception as e:
            print(f'Error sending message to Kafka: {e}')
            return HttpResponse('Error sending message to Kafka')

        response_data = {
            'message': 'Message sent to Kafka',
            'access_token': access_token,
            'mylogin-data': data
}
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    else:
        return HttpResponse('Invalid request method')
