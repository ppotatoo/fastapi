import requests


cid = input('What is the city ID?\n')
r = requests.delete(f'http://127.0.0.1:8000/cities?city_id={cid}').json()
print(r)