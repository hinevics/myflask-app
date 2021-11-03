from flask import Flask, app
from flask_mongoengine import MongoEngine

from pymongo import MongoClient

from app.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT
from app.datascript import db_start

db_start()

print('start create flask app')
server = Flask(__name__)


cluster = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = cluster[MONGO_DATABASE]
db_collections = db[MONGO_COLLECTION]

from app import authors, config, datascript, distribution_authors, models, routes

server.run()
