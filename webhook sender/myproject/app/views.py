from django.shortcuts import render
import json
import requests
from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseBadRequest, JsonResponse
import requests
import json
from flask import Flask, request, abort
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
import datetime
from datetime import datetime, timedelta
# Create your views here.

def message_box(request):
    return render(request, 'massenger.html')

def display_message(request):
    return render(request, 'notification.html')

@csrf_exempt
def message_reciever(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('message')
        
        if text is not None:
            data = Message(text=text, created_at=datetime.now())
            data.save()
            # Do something useful with the message, such as sending a notification
            print(f"Received message: {text}")
            
            return JsonResponse({'status': 'Message received'})
        else:
            return JsonResponse({'error': 'Message cannot be empty'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def receiving_chats(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        response_data = {'status': True, 'messages': list(messages.values())}
        return HttpResponse(json.dumps(response_data, cls=CustomJSONEncoder), content_type='application/json')
    elif request.method == 'POST':
        # Handle the POST request here
        return HttpResponse('Success!')

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

@csrf_exempt
def webhook_sender(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
        
            data = {
                'text': payload.get('message', ''),
                'created_at': datetime.now(),
            }
            message = Message(**data)
            message.save()

            url = 'http://localhost:8000/message_receiver/'  # Modify this URL according to your needs
            headers = {'Content-Type': 'application/json'}
            # Set the ID to 2
            response = requests.post(url,  headers=headers)
            if response.status_code == requests.codes.ok:
                print("Data sent successfully")
            else:
                print(f"Failed to send data. Response status code: {response.status_code}")
        
            webhook_receiver(payload)

            return JsonResponse({'message': 'Success'})

        except json.JSONDecodeError as e:
            return HttpResponseBadRequest("Invalid JSON payload.")
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def webhook_receiver(data):
    url = 'http://localhost:8005/messager_recieving/'  # Modify this URL according to your needs
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == requests.codes.ok:
            print("Data sent successfully")
        else:
            print(f"Failed to send data. Response status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {str(e)}")

