import requests
from pymongo import MongoClient

results : dict = {}
MONGO_URI = 'mongodb://localhost'
cliente = MongoClient(MONGO_URI)

db = cliente['rickandmorty']
collection = db['personajes']
for i in range(1,22):
    url = "https://rickandmortyapi.com/api/character?page=" + str(i)
    response = requests.get(url)
    data = response.json()
    results = data['results']
    collection.insert_many(results)






