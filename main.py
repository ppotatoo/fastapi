from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel
import json

app = FastAPI()

bob = {'bob': {
    'age': 29,
    'gender': 'male',
    'occupation': 'electrical engineer',
    'favorite food': 'tacos',
    'favorite color': 'magenta',
    'education level': 'phd in taco eating'
}}

db = []



class City(BaseModel):
    name: str
    state: str


@app.get('/')
def index():
    return {'key' : 'value'}

@app.get('/bob')
def hi_bob():
    return JSONResponse(status_code=200, content=bob)

@app.get('/cities')
def get_cities():
    return db


#@app.get('/cities/{city_id}')

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete('/cities')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {'message': 'cool.'}
