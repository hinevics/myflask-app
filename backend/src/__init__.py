from flask import Flask

from pymongo import MongoClient

from src.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT

server = Flask(__name__)
cluster = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = cluster[MONGO_DATABASE]
db_collections = db[MONGO_COLLECTION]

from src import authors, config, models, routes

server.run(host='0.0.0.0', port=8080)
