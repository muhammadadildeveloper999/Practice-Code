from django.test import TestCase

# Create your tests here.
# # Create a Kafka consumer instance for messages coming from Kafka topic

# def send_email(topic, email,password):
#     # try:
#         msg = MIMEMultipart()
#         msg['From'] = email
#         msg['To'] = email
#         msg['Subject'] = 'New Kafka message received'
#         body = f'New message received on Kafka topic "{topic}":\n\n{email}'
#         msg.attach(MIMEText(body, 'plain'))
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(email, password)# add your Gmail account password here 
#         print(password,'-------------------------------------------------------------------------------------------------password') 
#         server.sendmail(email, email, msg.as_string())
#         server.quit()
#         print('Email sent successfully')
#     # except Exception as e:
#     #     print(f'Error sending email: {e}')

#     # except Exception as e:
#     #     print(f'Error sending email: {e}')
# import re

# # regular expression to match valid email address format
# email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# def adil(consumer):
#     # consume messages from Kafka topic
#     for message in consumer:
#         # try:
#             if message is None:  # Check if message is None
#                 continue

#             # decode the message
#             message_str = message.value.decode()
#             if not message_str.strip(): # check if message is empty
#                 continue
            
#             try:
#                 data = json.loads(message_str)
#                 if not isinstance(data, dict):
#                     raise ValueError('Invalid message format: expected dictionary object')
#             except ValueError as e:
#                 print(f'Invalid message format: {e}')
#                 continue

#             # get the email address and topic from the message
#             # try:
#             email = data.get('email')
#             # if not re.match(email_regex, email):
#                 # raise ValueError('Invalid email address format')
#             topic = data.get('topic')
#             password = data.get('password')
#             print('password',password) 

#             # except (KeyError, TypeError, ValueError) as e:
#             #     print(f'Error getting email or topic from message: {e}')
#             #     continue
            
#             # send the email
#             send_email(topic, email,password)
#         # except Exception as e:
#         #     # handle exceptions
#         #     print(f'Error sending email: {e}')
#         #     continue

# # set up Kafka consumer
# consumer = KafkaConsumer('adil', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True)

# # automatically call my_topic() function whenever a new message is received
# adil(consumer)

# {"email": "muhammadadil436huh@gmail.com", "topic": "adil", "message": "Hello Kafka!", "password": "mokxizfzxtojkfnv"}
# chatgpt message jo  Hello Kafka! kafka topic per send horaha hai os mujhe gmail per send_email
# kerna hai yani jo kakfa topic per send horaha hai os ko mujhe gmail per send kerna hai

