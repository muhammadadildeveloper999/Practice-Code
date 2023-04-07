from django.test import TestCase

# Create your tests here.

# @csrf_exempt
# def webhooks(request):
#     if request.method == 'POST':

#         event_type = request.POST.get('event_type')
#         user_name = request.POST.get('user_name')
#         message = f'{user_name} just triggered event {event_type}!'
        
#         # Send a notification to your server
#         response = send_notification(message)

#         # Check the response and return a success or error response
#         if response.status_code == 200:
            
#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({'status': 'error'})
#     else:
#         return JsonResponse({'status': 'error'})


#  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class WebhookReceiver(APIView):
#     def post(self, request):
#         try:
#             data = json.loads(request.body.decode('utf-8'))
            
#             event_type = request.data.get('event_type')
#             user_name = request.data.get('user_name')
#             message = f'{user_name} just receive event {event_type}!'
            
#             notification = WebhookNotification.objects.create(
#                 event_type=event_type, 
#                 user_name=user_name, 
#                 message=message,
#                 date_created=datetime.now().date()
#             )
                        
#             return Response({"status":True,"message":"Success"},200)
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest('Invalid JSON data')


# class WebhookReceiver(APIView):
#     def post(self, request):
#         try:
#             data = json.loads(request.body.decode('utf-8'))
            
#             event_type = request.data.get('event_type')
#             user_name = request.data.get('user_name')
#             message = f'{user_name} just triggered event {event_type}!'
            
#             # Send a notification to your server
#             response = requests.post(
#                 'http://127.0.0.1:9000/notification/',
#                 data=json.dumps({'message': message}), 
#                 headers={'Content-Type': 'application/json'},
#                 timeout=None
#             )
            
#             # Check the response and return a success or error response
#             if response.ok:
#                 return Response({"status":True,"message":"Success"},200)
#             else:
#                 return Response({"status":False,"message":"Failed to send webhook notification"},500)

#         except json.JSONDecodeError:
#             return HttpResponseBadRequest('Invalid JSON data')

# @csrf_exempt
# def webhook_sender(request):
#     if request.method == 'POST':
#         try:                     
#             payload = json.loads(request.body)
#             print(payload)
#             # create a new WebhookNotification object and save it to the database
#             notifications = notification(payload=json.dumps(payload))
#             notifications.save()
            
#             # forward the request to port 8005 with the correct endpoint
#             forwarded_payload = json.dumps(payload)
#             response = requests.post('http://127.0.0.1:8005/webhook_sender', data=forwarded_payload)
            
#             return JsonResponse({'message': 'Success'})
        
#         except json.JSONDecodeError as e:
#             return HttpResponseBadRequest("Invalid JSON payload.")
#     else:
#         return HttpResponseBadRequest("Invalid request method.")
 

# import traceback

# @csrf_exempt
# def forward_request(request, url):
#     if request.method == 'POST':
#         try:
#             payload_str = request.body.decode('utf-8')
#             print(payload_str) # print payload received
#             payload = json.loads(payload_str)
#             print(payload) # print parsed JSON payload

#             if not payload:
#                 return HttpResponseBadRequest("Empty JSON payload.")
        
#             # create a new WebhookNotification object and save it to the database
#             notifications = notification(payload=json.dumps(payload))
#             notifications.save()

#             # Forward the request to the specified URL with the same payload
#             response = requests.post(url, json=payload)

#             # Return the response received from the destination server
#             return JsonResponse(response.json())
#         except Exception as e:
#             traceback.print_exc()
#             return HttpResponseBadRequest("Invalid JSON payload.")
#     else:
#         return HttpResponseBadRequest("Invalid request method.")

# @csrf_exempt
# def webhook_sender(request):
#     return forward_request(request, 'http://127.0.0.1:8005/webhook_receiver')


# @csrf_exempt
# def webhook_sender(request):
#     if request.method == 'POST':
#         try:
#             payload = json.loads(request.body)
#             print(payload)
#             # create a new WebhookNotification object and save it to the database
#             notifications = notification(payload=json.dumps(payload))
#             notifications.save()
            
#             # forward the request to the destination server
#             success = send_request(payload)
#             if success:
#                 return JsonResponse({'message': 'Success'})
#             else:
#                 return JsonResponse({'message': 'Failed to send request to destination server.'})
        
#         except json.JSONDecodeError as e:
#             return HttpResponseBadRequest("Invalid JSON payload.")
#     else:
#         return HttpResponseBadRequest("Invalid request method.")

# def send_request(payload):
#     forwarded_payload = json.dumps(payload)
#     response = requests.post('http://127.0.0.1:8005/webhook_sender', data=forwarded_payload)
#     if response.status_code == 200:
#         return True
#     else:
#         return False
#     yai hai webhook_sender mujhe yai kerna hai ke jese hi  webhook_sender ki  fuction call hu tu wo webhook_reciever
#     ke payload mai chale jaye or webhook_reciever oss ko reciever kerle please make a code example

# @csrf_exempt
# def webhook_send_message(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             # print(data)
#             webhook_recieve_message(data)  # Call the function to send data to another server
#             return JsonResponse({'message': 'Success'})
#         except json.JSONDecodeError as e:
#             return HttpResponseBadRequest("Invalid JSON payload.")
#     else:
#         return JsonResponse({'error': 'Invalid request method'})

# @csrf_exempt
# def webhook_recieve_message(data):
#     url = 'http://localhost:8005/receive_message/'  # Modify this URL according to your needs
#     headers = {'Content-Type': 'application/json'}
#     try:
#         response = requests.post(url, data=json.dumps(data), headers=headers)
#         if response.status_code == requests.codes.ok:
#             print("Data sent successfully")
#         else:
#             print(f"Failed to send data. Response status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"Error sending data: {str(e)}")

# @csrf_exempt
# def webhook_send_message(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             text = request.data.get('text')
#             # save the message to database
#             Message.objects.create(text=text)
#             # send the message to another server
#             webhook_recieve_message(data)
#             return JsonResponse({'message': 'Success'})
#         except json.JSONDecodeError as e:
#             return HttpResponseBadRequest("Invalid JSON payload.")
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
# AttributeError at /api/webhook_send_message/
# 'WSGIRequest' object has no attribute 'data'

# @csrf_exempt
# def webhook_recieve_message(data):
#     url = 'http://localhost:8005/receive_message/'  # Modify this URL according to your needs
#     headers = {'Content-Type': 'application/json'}
#     try:
#         response = requests.post(url, data=json.dumps(data), headers=headers)
#         if response.status_code == requests.codes.ok:
#             print("Data sent successfully")
#         else:
#             print(f"Failed to send data. Response status code: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"Error sending data: {str(e)}")




# <!-- <!DOCTYPE html>
# <html>
#   <head>
#     <title>Send Message</title>
#     <style>
#       body {
#         background-color: black;
#       }
      
#       .container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         height: 100vh;
#       }
      
#       .form-container {
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#         align-items: center;
#         background-color: #fff;
#         padding: 30px;
#         border-radius: 10px;
#         box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.2);
#       }
      
#       h1 {
#         font-size: 45px;
#         color: #000;
#         text-align: center;
#         font-family: 'Pacifico', cursive;
#         font-weight: 600;
#         margin-bottom: 30px;
#       }
      
#       form {
#         display: flex;
#         flex-direction: column;
#         align-items: center;
#         width: 100%;
#       }
      
#       label {
#         font-size: 30px;
#         color: #000;
#         margin-bottom: 10px;
#       }
      
#       input[type="text"] {
#         height: 30px;
#         width: 300px;
#         margin-bottom: 20px;
#         padding: 5px;
#         font-size: 20px;
#         border: 1px solid #ccc;
#         border-radius: 5px;
#       }
      
#       button[type="submit"] {
#         height: 30px;
#         width: 100px;
#         color: #fff;
#         font-size: 15px;
#         background-color: #333;
#         border: none;
#         border-radius: 5px;
#         cursor: pointer;
#       }
#     </style>
#   </head>
#   <body>
#     <div class="container">
#       <div class="form-container">
#         <h1>Send Message</h1>
#         <form id="send-message-form" method="POST" action="{% url 'webhook_send_message' %}">
#           {% csrf_token %}
#           <label for="message">Message:</label>
#           <input type="text" id="message" name="message" required>
#           <button type="submit" id="send-button">Send</button>
#         </form>
#       </div>
#     </div>
#     <script>
#       document.getElementById('send-message-form').addEventListener('submit', function(event) {
#         event.preventDefault();
#         var message = document.getElementById('message').value;
#         var data = { 'message': message };
#         fetch('{% url "webhook_send_message" %}', {
#           method: 'POST',
#           headers: { 'Content-Type': 'application/json' },
#           body: JSON.stringify(data)
#         })
#         .then(response => {
#           if (response.ok) {
#             window.location.replace("{% url 'recieve_message' %}");
#           } else {                                                    
#             console.log('Failed to send data. Response status code:', response.status);
#           }
#         })
#         .catch(error => {
#           console.log('Error sending data:', error);
#         });
#       });
#     </script>
#   </body>
# </html> -->

# fetch(apiUrl)
#      .then(response => response.json())
#      .then(data => {
#      console.log("use",data.messages);
#      var even=data.messages?.filter((num)=>{
#         return num
#      })
#      })
#      console.log("even",even)
#      .catch(error => {
#        console.error('Error fetching data:', error);
#      });








# <!DOCTYPE html>
# <html>

# <head>
#     <title>Message Receiver</title>
#     <style>
#         .message-box {
#             width: 400px;
#             height: 100px;
#             background-color: #f3f3f3;
#             border: 1px solid #ccc;
#             border-radius: 10px;
#             margin-left: 140px;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#         }

#         .message {
#             width: 260%;
#             height: 60%;
#             background-color: lightblue;
#             border-radius: 10px;
#             padding: 10px;
#             box-shadow: 0px 3px 3px rgba(0, 0, 0, 0.2);
#         }

#         .new-class {
#             background-color: lightgreen;
#         }

#         .message p {
#             margin: 0;
#             font-size: 25px;
#         }
#         .new{
#           color: red !important;
#         }

#     </style>
# </head>

# <body>
#     <div id="message-box" class="message-box">
#         <div class="message">
#             <p>This is a message box.</p>
#         </div>
#     </div>
#     <script>

#         var apiUrl = 'http://127.0.0.1:8000/api/receive_notification/';

#         fetch(apiUrl)
#         .then(response => response.json())
#         .then(data => {
#         console.log(data.messages);
#         var newdata = data.messages;
#         console.log(newdata, "newdata")
#   \


#         newdata.map((value, id)=>{
#           // console.log(value.text)  
#             document.write(`<h1 style="color: red;width: 300px;
#             height: 100px;
#             background-color: lightgrey;
#             display: flex;
#             align-items: center;">${"id",value.id, value.text}<h1/>`)
#         })

        
#         })
#         .catch(error => {
#           console.error('Error fetching data:', error);
#         });
#     </script>
#     <div class="row">
#       <div class="col-md-4">
# <div id="aDIL">

# </div>
#       </div>
#     </div>
# </body>

# </html>
