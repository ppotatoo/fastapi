import requests

r = requests.post('http://127.0.0.1:8000/cities', json={'name': 'PHDS', 'state': 'Fsdfsff'}).json()
print(r)