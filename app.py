from flask import Flask, render_template,jsonify
from pymongo import MongoClient
#importar datos del servidor
from extraer import results
from config import Config

app = Flask(__name__)
# app.config.from_object(Config)

MONGO_URI = 'mongodb://localhost'
cliente = MongoClient(MONGO_URI)

db = cliente['rickandmorty']
collection = db['personajes']

# collection.insert_many(results)

@app.route("/")
def index():
    data = collection.find({})
    return render_template("index.html" , data_personajes = data)


@app.route("/ruta_productos", methods=['GET'])
def ruta_productos():
    return jsonify(results)