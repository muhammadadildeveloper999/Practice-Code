import requests

URL = 'http://127.0.0.1:8000/Student_list/'

r = request.get(url = URL)

data = r.json()

mn print(data)
